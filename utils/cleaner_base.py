import re
import nltk
import contractions
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download("vader_lexicon")

# === NLTK Setup ===
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("averaged_perceptron_tagger")
nltk.download("wordnet")

lemmatizer = WordNetLemmatizer()
STOPWORDS = set(stopwords.words("english"))

def preclean_text(text):
    """Pre-clean text by removing metadata, non-ASCII chars, and extra whitespace."""
    text = re.sub(
        r"(?i)^(copyright|ages? \d+-\d+|teacher'?s guide|parent tips|published by|isbn|www\.|illustrated by).*?$",
        "",
        text,
        flags=re.MULTILINE
    )
    text = re.sub(r"[^\x00-\x7F]+", "", text)  # Remove non-ASCII characters
    text = re.sub(r"\s+", " ", text)           # Normalize whitespace
    return text.strip()

def get_wordnet_pos(tag):
    """Maps POS tags to WordNet format for lemmatization."""
    tag_dict = {"J": wordnet.ADJ, "N": wordnet.NOUN, "V": wordnet.VERB}
    return tag_dict.get(tag[0].upper(), wordnet.NOUN)
