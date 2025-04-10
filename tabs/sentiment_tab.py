import streamlit as st
import rubric.sentiment_emotion_rubric as svr
from rubric.interpreters.sentiment_interp import (
    interpret_compound_sentiment,
    interpret_emotion_profile
)

def render_sentiment_tab(cleaned_text, sentiment_scores, emotion_scores):
    st.subheader("💖 Sentiment & 🎭 Emotion")

    # === Cleaned Text
    st.markdown("### 🧼 Cleaned Text for Sentiment Analysis")
    st.text_area("Cleaned Sentiment Text", cleaned_text, height=200)

    # === Raw Sentiment (VADER)
    st.markdown("### 🧪 VADER Sentiment Scores")
    st.json(sentiment_scores)

    # === Raw Emotion (BERT)
    st.markdown("### 🎭 Emotion Scores (DistilRoBERTa)")
    if emotion_scores:
        st.json(emotion_scores)
    else:
        st.warning("🤖 No emotions detected. Try a more expressive or emotional story.")

    # === Interpretation
    st.markdown("### 🗣️ Interpretation Summary")
    st.write(f"**Sentiment (Compound Score):** {interpret_compound_sentiment(sentiment_scores.get('compound', 0))}")
    st.write(f"**Emotion Profile:** {interpret_emotion_profile(emotion_scores)}")

    # === Rubric
    st.markdown("### 📘 Sentiment & Emotion Rubric")
    with st.expander("📘 How to Interpret Sentiment & Emotional Scores"):
        st.markdown(svr.sentiment_emotion_rubric(), unsafe_allow_html=True)
