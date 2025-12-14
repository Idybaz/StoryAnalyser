import re
import contractions
from collections import Counter
from nltk import pos_tag, word_tokenize
from utils.cleaner_base import preclean_text, lemmatizer, get_wordnet_pos, STOPWORDS


def clean_for_thematic_analysis(text: str) -> str:
    """Clean text to extract core nouns and verbs for theme detection."""
    text = preclean_text(text)
    text = contractions.fix(text).lower()
    text = re.sub(r"[^\w\s]", "", text)

    words = word_tokenize(text)
    pos_tags = pos_tag(words)

    content_words = [
        lemmatizer.lemmatize(word, get_wordnet_pos(tag))
        for word, tag in pos_tags
        if tag.startswith(("N", "V")) and word not in STOPWORDS
    ]

    return " ".join(content_words)


def extract_top_words(text: str, top_n: int = 5) -> list:
    """Returns top N most frequent content words (simple frequency-based)."""
    cleaned = clean_for_thematic_analysis(text)
    word_counts = Counter(cleaned.split())
    return word_counts.most_common(top_n)


def extract_keywords_keybert(text: str, top_n: int = 5) -> list:
    """
    Extract top N keywords/phrases using KeyBERT (semantic analysis).
    Returns: list of tuples (keyword, score)

    Streamlit Cloud safe:
    - Lazy-imports KeyBERT
    - Lazy-loads the model
    - Falls back to frequency keywords if anything fails
    """
    if not text or not text.strip():
        return []

    try:
        from keybert import KeyBERT  # lazy import

        # Create model lazily inside function to avoid app crash on startup
        kw_model = KeyBERT("all-MiniLM-L6-v2")

        return kw_model.extract_keywords(
            text,
            keyphrase_ngram_range=(1, 2),
            stop_words="english",
            top_n=top_n
        )

    except Exception:
        # Fallback: return top words with a dummy score
        fallback = extract_top_words(text, top_n=top_n)
        return [(w, 0.0) for w, _ in fallback]
