import numpy as np
import re
from collections import Counter
import contractions
from nltk import pos_tag, word_tokenize
from utils.cleaner_base import preclean_text, lemmatizer, get_wordnet_pos, STOPWORDS

def clean_for_lexical_diversity(text):
    """Clean text for lexical richness analysis (TTR, MTLD, etc.)."""
    text = preclean_text(text)
    text = contractions.fix(text).lower()
    text = re.sub(r"[^\w\s']", "", text)

    words = word_tokenize(text)
    pos_tags = pos_tag(words)

    return ' '.join([
        lemmatizer.lemmatize(word, get_wordnet_pos(tag))
        for word, tag in pos_tags
        if word not in STOPWORDS and len(word) > 2
    ])

def analyze_lexical_diversity(text: str) -> dict:
    """
    Analyzes lexical diversity in children's storybooks using:
    - TTR (Type-Token Ratio)
    - MATTR (Moving Average Type-Token Ratio)
    - MTLD (Measure of Textual Lexical Diversity)
    - HDD (Hypergeometric Distribution Diversity)
    """
    words = word_tokenize(text)

    if len(words) < 5:
        return {"error": "Text too short for reliable analysis"}

    return {
        "ttr": _calculate_ttr(words),
        "mattr": _calculate_mattr(words),
        "mtld": _calculate_mtld(words),
        "hdd": _calculate_hdd(words),
    }

# === TTR: Type-Token Ratio ===
def _calculate_ttr(words: list) -> float:
    """Calculates the Type-Token Ratio."""
    return round(len(set(words)) / len(words), 3)

# === MATTR: Moving Average TTR ===
def _calculate_mattr(words: list) -> float:
    """Calculates MATTR with an adaptive window for children's books."""
    window_size = min(50, len(words) // 2)

    if len(words) < window_size:
        return _calculate_ttr(words)  # fallback to TTR

    tt_ratios = [
        len(set(words[i:i + window_size])) / window_size
        for i in range(len(words) - window_size + 1)
    ]

    return round(np.mean(tt_ratios), 3)

# === MTLD: Measure of Textual Lexical Diversity ===
def _calculate_mtld(words: list, threshold: float = 0.72) -> float:
    """
    Computes MTLD using McCarthy & Jarvis (2010) method.
    """
    def count_factors(words, threshold):
        factors = 0
        word_count = 0
        seen = set()

        for word in words:
            seen.add(word)
            word_count += 1
            ttr = len(seen) / word_count

            if ttr < threshold:
                factors += 1
                word_count = 0
                seen = set()

        return factors + (word_count / len(words)) if word_count > 0 else factors

    forward_mtld = count_factors(words, threshold)
    backward_mtld = count_factors(words[::-1], threshold)

    return float(round((len(words) / (forward_mtld + backward_mtld)) * 2, 3))

# === HDD: Hypergeometric Distribution Diversity ===
def _calculate_hdd(words: list, sample_size: int = 42) -> float:
    word_counts = Counter(words)
    total_types = len(word_counts)
    total_tokens = len(words)

    if total_types == 0:
        return 0.0

    sum_prob = sum(
        1 - np.prod([(count - i) / (total_tokens - i) for i in range(min(sample_size, total_tokens))])
        for count in word_counts.values()
    )

    return float(round(sum_prob / total_tokens, 3))
