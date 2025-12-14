import re
import numpy as np
import contractions
import spacy
from nltk.sentiment import SentimentIntensityAnalyzer
from utils.cleaner_base import preclean_text

# Optional emoji handling
try:
    import emoji
except ImportError:
    emoji = None

# Load spaCy + VADER once (these are relatively lightweight)
nlp = spacy.load("en_core_web_sm")
sia = SentimentIntensityAnalyzer()


def clean_for_sentiment(text: str) -> str:
    """Clean text for sentiment analysis, preserving emotional cues."""
    text = preclean_text(text)
    text = contractions.fix(text)
    text = re.sub(r"[^\w\s.,!?'…-]", "", text)

    if emoji is not None:
        text = emoji.replace_emoji(text, replace="")

    return text.strip()


def analyze_sentiment(text: str) -> dict:
    """Sentence-level sentiment using VADER (fast + offline)."""
    if not text or not text.strip():
        return {"compound": 0.0, "positive": 0.0, "neutral": 0.0, "negative": 0.0}

    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents] or [text]

    vader_scores = [sia.polarity_scores(sent) for sent in sentences]

    return {
        "compound": round(float(np.mean([s["compound"] for s in vader_scores])), 3),
        "positive": round(float(np.mean([s["pos"] for s in vader_scores])), 3),
        "neutral": round(float(np.mean([s["neu"] for s in vader_scores])), 3),
        "negative": round(float(np.mean([s["neg"] for s in vader_scores])), 3),
    }


# -------------------------
# Emotion model (HF) – lazy + cached
# -------------------------
def _get_emotion_classifier():
    """
    Returns a cached HF pipeline when running in Streamlit.
    If Streamlit isn't available (e.g., tests), falls back to uncached.
    """
    try:
        import streamlit as st

        @st.cache_resource(show_spinner=False)
        def _cached():
            from transformers import pipeline
            return pipeline(
                "text-classification",
                model="j-hartmann/emotion-english-distilroberta-base",
                return_all_scores=True,
            )

        return _cached()

    except Exception:
        # Not running in Streamlit or cache failed; try direct load
        from transformers import pipeline
        return pipeline(
            "text-classification",
            model="j-hartmann/emotion-english-distilroberta-base",
            return_all_scores=True,
        )


def analyze_emotion(text: str) -> dict:
    """
    Emotion analysis using pretrained DistilRoBERTa.
    Cloud-safe: if model can't load/run, returns {} instead of crashing.
    """
    if not text or not text.strip():
        return {}

    # Build sentences (short chunks work better than whole documents)
    doc = nlp(text)
    sentences = [sent.text.strip() for sent in doc.sents if sent.text.strip()] or [text.strip()]

    try:
        emotion_classifier = _get_emotion_classifier()
    except Exception:
        # Can't download/load HF model in this environment
        return {}

    all_results = []
    for sentence in sentences:
        try:
            # keep within transformer input limits
            results = emotion_classifier(sentence[:512])[0]
            all_results.append({r["label"]: float(r["score"]) for r in results})
        except Exception:
            continue

    if not all_results:
        return {}

    labels = all_results[0].keys()
    return {label: round(float(np.mean([res[label] for res in all_results])), 3) for label in labels}
