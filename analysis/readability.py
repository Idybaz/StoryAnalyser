import re
import contractions
import textstat
from utils.cleaner_base import preclean_text


def clean_for_readability(text: str) -> str:
    """Prepare text for readability metrics like Flesch-Kincaid."""
    text = preclean_text(text)
    text = contractions.fix(text)

    # Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()

    # Optional: sentence breaks help some metrics
    text = re.sub(r"([.!?]) +", r"\1\n", text)

    # Keep basic punctuation only
    text = re.sub(r"[^\w\s.,!?\"'-]", "", text)

    return text.strip()


def _safe_metric(fn, cleaned: str, ndigits=2):
    """Run a metric safely; return None if it fails."""
    try:
        val = fn(cleaned)
        # textstat sometimes returns strings; coerce if needed
        return round(float(val), ndigits)
    except Exception:
        return None


def analyze_readability(text: str) -> dict:
    """Analyzes readability using multiple metrics."""
    if not text or not text.strip():
        return {
            "spache_score": None,
            "flesch_reading_ease": None,
            "flesch_kincaid_grade": None,
            "dale_chall_score": None
        }

    cleaned = clean_for_readability(text)
    if not cleaned:
        return {
            "spache_score": None,
            "flesch_reading_ease": None,
            "flesch_kincaid_grade": None,
            "dale_chall_score": None
        }

    return {
        "flesch_reading_ease": _safe_metric(textstat.flesch_reading_ease, cleaned),
        "flesch_kincaid_grade": _safe_metric(textstat.flesch_kincaid_grade, cleaned),
        "spache_score": _safe_metric(textstat.spache_readability, cleaned),
        "dale_chall_score": _safe_metric(textstat.dale_chall_readability_score, cleaned),
    }
