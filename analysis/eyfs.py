import re
from collections import defaultdict
from sentence_transformers import SentenceTransformer, util
from utils.dictionary import EYFS_themes_dict


# === Load model once ===
model = SentenceTransformer("all-MiniLM-L6-v2")


# === Prepare theme labels and embeddings ===
eyfs_opportunities = {}

for area, subthemes in EYFS_themes_dict.items():
    for subtheme, content in subthemes.items():
        label = f"{area} > {subtheme}"
        eyfs_opportunities[label] = content["description"]

theme_labels = list(eyfs_opportunities.keys())
theme_texts = list(eyfs_opportunities.values())
theme_embeddings = model.encode(theme_texts, convert_to_tensor=True)


# === BERT-Based Matching ===
def match_eyfs_opportunities(text, model=model, theme_embeddings=theme_embeddings, theme_labels=theme_labels, top_n=3):
    story_embedding = model.encode(text, convert_to_tensor=True)
    similarity_scores = util.cos_sim(story_embedding, theme_embeddings)[0]
    top_matches = similarity_scores.argsort(descending=True)[:top_n]
    return [theme_labels[i] for i in top_matches]


def get_theme_scores(text, model=model, theme_embeddings=theme_embeddings, theme_labels=theme_labels):
    story_embedding = model.encode(text, convert_to_tensor=True)
    similarity_scores = util.cos_sim(story_embedding, theme_embeddings)[0]
    return dict(zip(theme_labels, similarity_scores.tolist()))


def get_most_prominent_theme(score_dict):
    return max(score_dict, key=score_dict.get) if score_dict else None


# === Optional Keyword-Based Matching (for reference or fallback) ===
def match_eyfs_keywords(text, eyfs_dict=EYFS_themes_dict):
    text = text.lower()
    matched = defaultdict(list)

    for area, subthemes in eyfs_dict.items():
        for subtheme, data in subthemes.items():
            for keyword in data["keywords"]:
                if re.search(rf"\b{re.escape(keyword)}\b", text):
                    matched[area].append(subtheme)
                    break

    return dict(matched)


def extract_main_theme_area_subtheme(matched_dict):
    if not matched_dict:
        return "", "", ""

    opportunities = list(matched_dict.keys())
    main_area, subthemes = max(matched_dict.items(), key=lambda x: len(x[1]))
    main_subtheme = subthemes[0] if subthemes else ""
    main_theme_full = f"{main_area} > {main_subtheme}" if main_subtheme else main_area

    return ", ".join(opportunities), main_area, main_theme_full
