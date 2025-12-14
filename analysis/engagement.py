import re
from collections import Counter

import contractions
from nltk import word_tokenize
from nltk.util import ngrams
from nltk.corpus import stopwords

from metaphone import doublemetaphone
import pronouncing

from utils.cleaner_base import preclean_text

# --- Optional: spaCy (don’t hard-crash if missing on Streamlit Cloud) ---
try:
    import spacy
    try:
        _NLP = spacy.load("en_core_web_sm")
    except Exception:
        _NLP = None
except Exception:
    spacy = None
    _NLP = None


def clean_for_engagement(text: str) -> str:
    """Prepare text for analyzing engagement: sound effects, interactivity, etc."""
    text = preclean_text(text or "")
    text = re.sub(r"([^\n])\n([^\n])", r"\1 \2", text)  # Merge broken lines
    text = contractions.fix(text)
    text = re.sub(r"[^\w\s.,!?'-]", "", text)
    return text.strip()


def analyze_engagement(text: str) -> dict:
    """Analyzes engagement features in preschool storybooks (ages 3-5)."""
    cleaned = clean_for_engagement(text)

    # If spaCy available, use it; otherwise use a simple fallback sentence split
    if _NLP is not None:
        doc = _NLP(cleaned)
        question_ratio = _count_questions_spacy(doc)
    else:
        question_ratio = _count_questions_fallback(cleaned)

    return {
        "repetition_score": _analyze_repetition(cleaned),
        "rhyme_score": _analyze_rhyme(cleaned),
        "question_ratio": question_ratio,
        "sound_effect_density": _detect_sound_effects(cleaned),
    }


# === Repetition ===
def _analyze_repetition(text: str, min_ngram: int = 2, max_ngram: int = 4) -> float:
    """Measures phrase repetition density using n-grams."""
    words = [w.lower() for w in word_tokenize(text) if w.isalpha()]
    total_words = len(words)

    # stopwords can fail if NLTK data isn't downloaded
    try:
        sw = set(stopwords.words("english"))
    except LookupError:
        sw = set()

    words = [w for w in words if w not in sw]

    phrase_counts = Counter()
    for n in range(min_ngram, max_ngram + 1):
        phrase_counts.update(" ".join(g) for g in ngrams(words, n))

    repeated_phrases = sum(count for _, count in phrase_counts.items() if count > 1)
    return round(repeated_phrases / max(1, total_words), 4)


# === Rhyme ===
def _analyze_rhyme(text: str, window: int = 6) -> float:
    """Computes rhyme density by detecting similar-sounding words."""
    words = [w.lower() for w in word_tokenize(text) if w.isalpha()]
    n = len(words)
    if n == 0:
        return 0.0

    def rhyme_part(word: str) -> str:
        phones = pronouncing.phones_for_word(word)
        if phones:
            return pronouncing.rhyming_part(phones[0]) or ""
        # metaphone fallback (may be empty)
        return doublemetaphone(word)[0] or ""

    # Precompute rhyme parts once (big speed win)
    parts = [rhyme_part(w) for w in words]

    rhymes = 0
    for i in range(n):
        pi = parts[i]
        if not pi:
            continue
        upper = min(i + window + 1, n)
        for j in range(i + 1, upper):
            if pi and pi == parts[j]:
                rhymes += 1

    return round(rhymes / max(1, n), 4)


# === Question Ratio ===
def _count_questions_spacy(doc) -> float:
    """Calculates the proportion of sentences that are questions (spaCy)."""
    sents = list(doc.sents)
    num_sentences = max(1, len(sents))
    num_questions = sum(1 for s in sents if s.text.strip().endswith("?") or "?" in s.text)
    return round(num_questions / num_sentences, 4)


def _count_questions_fallback(text: str) -> float:
    """Fallback question ratio without spaCy."""
    # crude sentence split
    sentences = [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]
    num_sentences = max(1, len(sentences))
    # count question marks in original text as a proxy
    num_questions = text.count("?")
    # treat each '?' as at most one question sentence
    num_questions = min(num_questions, num_sentences)
    return round(num_questions / num_sentences, 4)


# === Sound Effect Density ===
def _detect_sound_effects(text: str) -> float:
    """Detects sound effects using uppercase patterns, repeated letters, and exclamations."""
    tokens = word_tokenize(text)
    total = len(tokens)
    if total == 0:
        return 0.0

    sound_effects = 0
    for tok in tokens:
        # Preserve BOOM, SPLASH, etc.
        if tok.isupper() and len(tok) > 2:
            sound_effects += 1
            continue

        # Exclamations as emotional emphasis
        if tok.endswith("!"):
            sound_effects += 1
            continue

        # Repeated letters: only count if 3+ repeats like "sooo" or "yaaay"
        if re.search(r"(.)\1\1+", tok.lower()):
            sound_effects += 1
            continue

    return round(sound_effects / max(1, total), 4)
