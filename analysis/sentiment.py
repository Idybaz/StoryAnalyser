import re
import contractions
import numpy as np
import spacy
from nltk.sentiment import SentimentIntensityAnalyzer
from utils.cleaner_base import preclean_text
from transformers import pipeline

# === Optional: Emoji handling ===
try:
    import emoji
except ImportError:
    emoji = None  # Fallback if emoji module is not installed

# === Initialize NLP tools ===
nlp = spacy.load("en_core_web_sm")
sia = SentimentIntensityAnalyzer()

# Load Hugging Face BERT-based emotion pipeline
emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)

# === Cleaning Function ===
def clean_for_sentiment(text):
    """Clean text for sentiment analysis, preserving emotional cues."""
    text = preclean_text(text)
    text = contractions.fix(text)
    text = re.sub(r"[^\w\s.,!?'…-]", "", text)

    if emoji:
        text = emoji.replace_emoji(text, replace="")  # Remove emojis if library is available

    return text.strip()

# === Sentiment Analysis Function ===
def analyze_sentiment(text: str) -> dict:
    """
    Sentence-level sentiment analysis using VADER.
    - Designed for children's books (<500 words)
    - Aggregates sentiment across sentences
    """
    if not text.strip():
        return {
            "compound": 0.0,
            "positive": 0.0,
            "neutral": 0.0,
            "negative": 0.0
        }

    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents] or [text]  # fallback if sentence split fails

    vader_scores = [sia.polarity_scores(sent) for sent in sentences]

    return {
        "compound": round(np.mean([s["compound"] for s in vader_scores]), 3),
        "positive": round(np.mean([s["pos"] for s in vader_scores]), 3),
        "neutral": round(np.mean([s["neu"] for s in vader_scores]), 3),
        "negative": round(np.mean([s["neg"] for s in vader_scores]), 3)
    }

def analyze_emotion(text: str) -> dict:
    """
    Emotion analysis using pretrained DistilRoBERTa.
    Handles long text by splitting into sentences and averaging scores.
    """
    if not text.strip():
        return {}

    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents if sent.text.strip()]
    if not sentences:
        sentences = [text]

    all_results = []

    for sentence in sentences:
        try:
            results = emotion_classifier(sentence[:512])[0]  # Truncate if needed
            all_results.append({r["label"]: r["score"] for r in results})
        except Exception as e:
            continue  # Skip any sentence that causes an issue

    if not all_results:
        return {}

    # Average the scores for each label
    averaged = {}
    for label in all_results[0].keys():
        averaged[label] = round(np.mean([res[label] for res in all_results]), 3)

    return averaged
