import re
import contractions
import textstat
from utils.cleaner_base import preclean_text

def clean_for_readability(text):
    """Prepare text for readability metrics like Flesch-Kincaid."""
    text = preclean_text(text)
    text = contractions.fix(text)
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"([.!?]) +", r"\1\n", text)
    text = re.sub(r"[^\w\s.,!?\"'-]", "", text)
    return text.strip()


def analyze_readability(text: str) -> dict:
    """Analyzes readability using multiple metrics."""
    if not text.strip():
        return {
            "spache_score": None,
            "flesch_reading_ease": None,
            "flesch_kincaid_grade": None,
            "dale_chall_score": None
        }

    cleaned = clean_for_readability(text)

    return {
        "flesch_reading_ease": round(textstat.flesch_reading_ease(cleaned), 2),
        "flesch_kincaid_grade": round(textstat.flesch_kincaid_grade(cleaned), 2),
        "spache_score": round(textstat.spache_readability(cleaned), 2),
        "dale_chall_score": round(textstat.dale_chall_readability_score(cleaned), 2)
    }