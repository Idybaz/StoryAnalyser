import re
import contractions
import re
import nltk
import numpy as np
from collections import Counter
from nltk import word_tokenize
from nltk.util import ngrams
from nltk.corpus import stopwords
from metaphone import doublemetaphone
import pronouncing
import spacy
from utils.cleaner_base import preclean_text

nlp = spacy.load("en_core_web_sm") 

def clean_for_engagement(text):
    """Prepare text for analyzing engagement: sound effects, interactivity, etc."""
    text = preclean_text(text)
    text = re.sub(r'([^\n])\n([^\n])', r'\1 \2', text)  # Merge broken lines
    text = re.sub(r"[^\w\s.,!?'-]", "", text)
    text = contractions.fix(text)
    text = re.sub(r"\b([A-Z]{2,})\b", lambda m: m.group(), text)  # Preserve BOOM!, SPLASH!
    return text.strip()

def analyze_engagement(text: str) -> dict:
    """Analyzes engagement features in preschool storybooks (ages 3-5)."""
    doc = nlp(text)

    return {
        "repetition_score": _analyze_repetition(text),
        "rhyme_score": _analyze_rhyme(text),
        "question_ratio": _count_questions(doc),
        "sound_effect_density": _detect_sound_effects(text),
    }

# === Repetition ===
def _analyze_repetition(text: str, min_ngram=2, max_ngram=4) -> float:
    """Measures phrase repetition density using n-grams."""
    words = [w.lower() for w in word_tokenize(text) if w.isalpha()]
    total_words = len(words)

    sw = set(stopwords.words("english"))
    words = [w for w in words if w not in sw]

    phrase_counts = Counter()
    for n in range(min_ngram, max_ngram + 1):
        phrase_counts.update([" ".join(gram) for gram in ngrams(words, n)])

    repeated_phrases = sum(count for phrase, count in phrase_counts.items() if count > 1)

    return round(repeated_phrases / max(1, total_words), 4)

# === Rhyme ===
def _analyze_rhyme(text: str, window=6) -> float:
    """Computes rhyme density by detecting similar-sounding words."""
    words = [w.lower() for w in word_tokenize(text) if w.isalpha()]
    rhymes = 0

    def get_rhyme_part(word):
        phones = pronouncing.phones_for_word(word)
        if phones:
            return pronouncing.rhyming_part(phones[0])
        return doublemetaphone(word)[0]

    for i in range(len(words)):
        for j in range(i + 1, min(i + window + 1, len(words))):
            if get_rhyme_part(words[i]) == get_rhyme_part(words[j]) and get_rhyme_part(words[i]):
                rhymes += 1

    return round(rhymes / max(1, len(words)), 4)

# === Question Ratio ===
def _count_questions(doc) -> float:
    """Calculates the proportion of sentences that are questions."""
    num_sentences = max(1, len(list(doc.sents)))

    num_questions = sum(
        1 for sent in doc.sents
        if sent.text.strip().endswith("?") or "?" in sent.text
    )

    return round(num_questions / num_sentences, 4)

# === Sound Effect Density ===
def _detect_sound_effects(text: str) -> float:
    """Detects sound effects using uppercase patterns, repeated letters, and exclamations."""
    words = word_tokenize(text)
    total_words = len(words)
    sound_effects = 0

    for word in words:
        if word.isupper() and len(word) > 2:
            sound_effects += 1
        elif any(word[i] == word[i+1] for i in range(len(word)-1)):
            sound_effects += 1
        elif word.endswith("!"):
            sound_effects += 1

    return round(sound_effects / max(1, total_words), 4)