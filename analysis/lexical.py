import re
import numpy as np
import contractions
from collections import Counter
from nltk import pos_tag, word_tokenize
from scipy.stats import hypergeom

from utils.cleaner_base import preclean_text, lemmatizer, get_wordnet_pos, STOPWORDS


def _tokenize_clean(text: str) -> list[str]:
    """Return cleaned, lemmatized tokens suitable for lexical diversity metrics."""
    text = preclean_text(text)
    text = contractions.fix(text).lower()
    text = re.sub(r"[^\w\s']", " ", text)

    words = word_tokenize(text)
    pos_tags = pos_tag(words)

    tokens = []
    for word, tag in pos_tags:
        if not word.isalpha():
            continue
        if word in STOPWORDS:
            continue
        if len(word) <= 2:
            continue
        lemma = lemmatizer.lemmatize(word, get_wordnet_pos(tag))
        if lemma and lemma not in STOPWORDS and len(lemma) > 2:
            tokens.append(lemma)

    return tokens


def clean_for_lexical_diversity(text: str) -> str:
    """If you still want a cleaned string (e.g., for display/debug)."""
    return " ".join(_tokenize_clean(text))


def analyze_lexical_diversity(text: str) -> dict:
    """
    Computes:
    - TTR
    - MATTR
    - MTLD
    - HD-D (Hypergeometric Distribution Diversity)
    """
    if not text or not text.strip():
        return {"ttr": None, "mattr": None, "mtld": None, "hdd": None}

    tokens = _tokenize_clean(text)

    # Too short => unreliable
    if len(tokens) < 20:
        return {
            "ttr": _calculate_ttr(tokens) if tokens else None,
            "mattr": None,
            "mtld": None,
            "hdd": None,
            "warning": "Text too short for reliable lexical diversity (need ~20+ tokens after cleaning).",
        }

    return {
        "ttr": _calculate_ttr(tokens),
        "mattr": _calculate_mattr(tokens, window_size=50),
        "mtld": _calculate_mtld(tokens, threshold=0.72),
        "hdd": _calculate_hdd(tokens, sample_size=42),
    }


def _calculate_ttr(tokens: list[str]) -> float:
    return round(len(set(tokens)) / max(1, len(tokens)), 3)


def _calculate_mattr(tokens: list[str], window_size: int = 50) -> float:
    # Standard MATTR uses a fixed window (often 50). If text shorter, just use TTR.
    if len(tokens) <= window_size:
        return _calculate_ttr(tokens)

    ttrs = []
    for i in range(0, len(tokens) - window_size + 1):
        window = tokens[i : i + window_size]
        ttrs.append(len(set(window)) / window_size)

    return round(float(np.mean(ttrs)), 3)


def _calculate_mtld(tokens: list[str], threshold: float = 0.72) -> float:
    """
    MTLD per McCarthy & Jarvis (2010), using forward + reverse average.
    """
    def mtld_pass(seq: list[str]) -> float:
        factors = 0
        types = set()
        token_count = 0

        for tok in seq:
            token_count += 1
            types.add(tok)
            ttr = len(types) / token_count

            if ttr <= threshold:
                factors += 1
                types = set()
                token_count = 0

        # partial factor: how close we got to threshold at the end
        if token_count > 0:
            current_ttr = len(types) / token_count
            # If current_ttr is still above threshold, partial factor < 1
            if current_ttr != 1:
                partial = (1 - current_ttr) / (1 - threshold)
            else:
                partial = 0.0
            factors += partial

        # avoid divide-by-zero
        return len(seq) / max(factors, 1e-9)

    forward = mtld_pass(tokens)
    backward = mtld_pass(tokens[::-1])
    return round(float((forward + backward) / 2), 3)


def _calculate_hdd(tokens: list[str], sample_size: int = 42) -> float:
    """
    HD-D (Hypergeometric Distribution Diversity).
    For each type with frequency f, compute P(type appears at least once in a sample of size N),
    then average across tokens per McCarthy & Jarvis style.
    """
    N = min(sample_size, len(tokens))
    counts = Counter(tokens)
    total_tokens = len(tokens)

    if total_tokens == 0 or N <= 0:
        return 0.0

    # Probability type appears at least once in sample:
    # 1 - P(0 successes) where successes=f, population=total_tokens, draws=N
    hdd_sum = 0.0
    for f in counts.values():
        # hypergeom(M=population, n=successes, N=draws).pmf(k)
        p0 = hypergeom(M=total_tokens, n=f, N=N).pmf(0)
        hdd_sum += (1.0 - p0)

    # Normalize to be in a comparable range (common: divide by N)
    return round(float(hdd_sum / N), 3)
