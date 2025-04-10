import streamlit as st
from analysis.readability import clean_for_readability, analyze_readability
from analysis.lexical import clean_for_lexical_diversity, analyze_lexical_diversity
from analysis.thematic import clean_for_thematic_analysis, extract_top_words, extract_keywords_keybert
from analysis.engagement import clean_for_engagement, analyze_engagement
from analysis.sentiment import clean_for_sentiment, analyze_sentiment, analyze_emotion
from analysis.eyfs import match_eyfs_opportunities, get_theme_scores, get_most_prominent_theme
from normalized.normalize_readability import normalize_readability_scores
from normalized.normalize_lexical import normalize_lexical_scores
from normalized.normalize_engagement import normalize_engagement_scores
from tabs.readability_tab import render_readability_tab
from tabs.lexical_tab import render_lexical_tab
from tabs.thematic_tab import render_thematic_tab
from tabs.engagement_tab import render_engagement_tab
from tabs.sentiment_tab import render_sentiment_tab
from tabs.eyfs_tab import render_eyfs_tab



# Check session state
if "precleaned" not in st.session_state:
    st.warning("🚧 No story processed yet. Please go to the **Upload Story** page first.")
    st.stop()

# Retrieve data
book_title = st.session_state["book_title"]
precleaned = st.session_state["precleaned"]

# Setup
st.set_page_config(page_title="📊 Analysis Results", layout="centered")
st.title(f"📊 Analysis Results: {book_title}")

# === Clean Text for Each Module ===
readable_ready = clean_for_readability(precleaned)
lexical_ready = clean_for_lexical_diversity(precleaned)
thematic_ready = clean_for_thematic_analysis(precleaned)
sentiment_ready = clean_for_sentiment(precleaned)
engagement_ready = clean_for_engagement(precleaned)

# === Run Metric Functions ===
readability_scores = analyze_readability(readable_ready)
lexical_scores = analyze_lexical_diversity(lexical_ready)
sentiment_scores = analyze_sentiment(sentiment_ready)
emotion_scores = analyze_emotion(sentiment_ready)
engagement_scores = analyze_engagement(engagement_ready)
top_words = extract_top_words(thematic_ready)
keybert_keywords = extract_keywords_keybert(thematic_ready, top_n=5)
eyfs_matches = match_eyfs_opportunities(precleaned)
eyfs_scores = get_theme_scores(precleaned)
eyfs_main_theme = get_most_prominent_theme(eyfs_scores)
adapted_readability_scores = normalize_readability_scores(readability_scores)
adapted_lexical_scores = normalize_lexical_scores(lexical_scores)
adapted_engagement_scores = normalize_engagement_scores(engagement_scores)


# === Layout Tabs ===
tabs = st.tabs(["📘 Readability", "🧠 Lexical", "🔍 Thematic", "💖 Sentiment", "🎶 Engagement", "🌱 EYFS"])

# === 📘 Tab: Readability ===
with tabs[0]:
    render_readability_tab(readable_ready, readability_scores, adapted_readability_scores)

# === 🧠 Tab: Lexical Diversity ===
with tabs[1]:
    render_lexical_tab(lexical_ready, lexical_scores, adapted_lexical_scores)

# === 🔍 Tab: Thematic ===
with tabs[2]:
    render_thematic_tab(thematic_ready, top_words, keybert_keywords)

# === 🎶 Tab: Engagement ===
with tabs[3]:
    render_engagement_tab(engagement_ready, engagement_scores, adapted_engagement_scores)

# === 💖 Tab: Sentiment & Emotion ===
with tabs[4]:
    render_sentiment_tab(sentiment_ready, sentiment_scores, emotion_scores)

# === 🌱 Tab: EYFS Thematic Mapping ===
with tabs[5]:
    render_eyfs_tab(precleaned, eyfs_main_theme, eyfs_scores)


# === Download Button ===
st.download_button(
    label="💾 Download Cleaned Text",
    data=precleaned,
    file_name=f"{book_title.replace(' ', '_')}_cleaned.txt"
)
