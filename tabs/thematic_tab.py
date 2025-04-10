import streamlit as st
import rubric.thematic_rubric as tr
from rubric.interpreters.thematic_interp import (
    interpret_top_words,
    interpret_keybert_phrases
)

def render_thematic_tab(cleaned_text, top_words, keybert_keywords):
    st.subheader("🔍 Thematic Content")

    # === Cleaned Text ===
    st.markdown("### 🧼 Cleaned Text for Theme Analysis")
    st.text_area("Thematic Cleaned Text", cleaned_text, height=200)

    # === Top 5 Frequent Words
    st.markdown("### 🧠 Most Frequent Theme Words")
    st.caption("These are the most common action or object words in the story.")
    if top_words:
        st.write(", ".join(f"`{word}`" for word, _ in top_words))
    else:
        st.warning("⚠️ No dominant content words found.")

    # === KeyBERT Phrases
    st.markdown("### 💡 Key Theme Phrases (AI-Extracted)")
    st.caption("AI-generated key ideas — reflect semantic meaning, not just frequency.")
    if keybert_keywords:
        for phrase, score in keybert_keywords:
            st.markdown(f"- **{phrase}** _(confidence: {round(score, 2)})_")
    else:
        st.warning("⚠️ No key phrases extracted.")

    # === Interpretation Summary
    st.markdown("### 🗣️ Thematic Interpretation")
    st.write(interpret_top_words(top_words))
    st.write(interpret_keybert_phrases(keybert_keywords))

    # === Rubric
    st.markdown("### 📘 Thematic Rubric")
    with st.expander("📘 How to Understand the Themes & Keywords"):
        st.markdown(tr.thematic_rubric(), unsafe_allow_html=True)
