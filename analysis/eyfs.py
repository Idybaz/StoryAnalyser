import re
from collections import defaultdict
from utils.dictionary import EYFS_themes_dict

# --- Optional import: don't crash the whole app if missing on Cloud ---
try:
    from sentence_transformers import SentenceTransformer, util
except Exception:
    SentenceTransformer = None
    util = None


def _build_theme_texts(eyfs_dict=EYFS_themes_dict):
    """Return (labels, texts) for EYFS theme descriptions."""
    opportunities = {}
    for area, subthemes in eyfs_dict.items():
        for subtheme, content in subthemes.items():
            label = f"{area} > {subtheme}"
            opportunities[label] = content.get("description", "")
    labels = list(opportunities.keys())
    texts = list(opportunities.values())
    return labels, texts


# --- Streamlit caching for heavy resources ---
def get_model_and_embeddings():
    """
    Returns (model, theme_embeddings, theme_labels).
    Uses Streamlit caching if available; otherwise does a plain load.
    """
    # Local import so non-streamlit environments don't break
    try:
        import streamlit as st
    except Exception:
        st = None

    theme_labels, theme_texts = _build_theme_texts()

    # If sentence-transformers is not available, signal fallback
    if SentenceTransformer is None or util is None:
        return None, None, theme_labels

    # If Streamlit is available, cache the heavy objects
    if st is not None:
        @st.cache_resource(show_spinner=False)
        def _cached():
            model = SentenceTransformer("all-MiniLM-L6-v2")
            theme_embeddings = model.encode(theme_texts, convert_to_tensor=True)
            return model, theme_embeddings, theme_labels

        return _cached()

    # Non-streamlit fallback (no caching)
    model = SentenceTransformer("all-MiniLM-L6-v2")
    theme_embeddings = model.encode(theme_texts, convert_to_tensor=True)
    return model, theme_embeddings, theme_labels


# === BERT-Based Matching ===
def match_eyfs_opportunities(text: str, top_n: int = 3):
    """
    Semantic matching using SentenceTransformer if available.
    Falls back to keyword matching if embeddings can't load.
    """
    model, theme_embeddings, theme_labels = get_model_and_embeddings()

    if model is None or theme_embeddings is None or util is None:
        # fallback: keyword matching
        matched = match_eyfs_keywords(text)
        # flatten into "Area > Subtheme" style
        flattened = []
        for area, subs in matched.items():
            for s in subs:
                flattened.append(f"{area} > {s}")
        return flattened[:top_n]

    story_embedding = model.encode(text, convert_to_tensor=True)
    similarity_scores = util.cos_sim(story_embedding, theme_embeddings)[0]
    top_idx = similarity_scores.argsort(descending=True)[:top_n]
    return [theme_labels[int(i)] for i in top_idx]


def get_theme_scores(text: str):
    """
    Returns dict[label] = similarity score (float).
    If semantic model unavailable, returns empty dict (or you can return keyword hits).
    """
    model, theme_embeddings, theme_labels = get_model_and_embeddings()

    if model is None or theme_embeddings is None or util is None:
        return {}

    story_embedding = model.encode(text, convert_to_tensor=True)
    similarity_scores = util.cos_sim(story_embedding, theme_embeddings)[0]
    return {label: float(similarity_scores[i]) for i, label in enumerate(theme_labels)}


def get_most_prominent_theme(score_dict: dict):
    return max(score_dict, key=score_dict.get) if score_dict else None


# === Keyword-Based Matching (fallback / reference) ===
def match_eyfs_keywords(text: str, eyfs_dict=EYFS_themes_dict):
    text = (text or "").lower()
    matched = defaultdict(list)

    for area, subthemes in eyfs_dict.items():
        for subtheme, data in subthemes.items():
            for keyword in data.get("keywords", []):
                if re.search(rf"\b{re.escape(keyword.lower())}\b", text):
                    matched[area].append(subtheme)
                    break

    return dict(matched)


def extract_main_theme_area_subtheme(matched_dict: dict):
    if not matched_dict:
        return "", "", ""

    opportunities = list(matched_dict.keys())
    main_area, subthemes = max(matched_dict.items(), key=lambda x: len(x[1]))
    main_subtheme = subthemes[0] if subthemes else ""
    main_theme_full = f"{main_area} > {main_subtheme}" if main_subtheme else main_area

    return ", ".join(opportunities), main_area, main_theme_full
