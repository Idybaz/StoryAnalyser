import streamlit as st
import rubric.engagement_rubric as er
from rubric.interpreters.engagement_interp import (
    interpret_repetition_score,
    interpret_rhyme_score,
    interpret_question_score,
    interpret_sound_effect_score,
    interpret_engagement_composite
)


def render_engagement_tab(cleaned_text, raw_scores, adapted_scores):
    st.subheader("🎶 Engagement Features")

    # === Cleaned Text ===
    st.markdown("### 🧼 Cleaned Text for Engagement Analysis")
    st.text_area("Engagement Cleaned Text", cleaned_text, height=200)

    # === Raw Scores ===
    st.markdown("### 📊 Raw Engagement Scores")
    st.json({
        "Repetition Score": raw_scores.get("repetition_score", "N/A"),
        "Rhyme Score": raw_scores.get("rhyme_score", "N/A"),
        "Question Ratio": raw_scores.get("question_ratio", "N/A"),
        "Sound Effect Density": raw_scores.get("sound_effect_density", "N/A")
    })

    # === Adapted Scores ===
    st.markdown("### 🧠 Adapted Developmental Scores (0–1)")
    st.caption("✅ Interpreted by developmental benefit: rhythm, participation, expressiveness.")
    st.json({
        "Repetition (Adapted)": adapted_scores.get("Repetition (Adapted)", "N/A"),
        "Rhyme (Adapted)": adapted_scores.get("Rhyme (Adapted)", "N/A"),
        "Questions (Adapted)": adapted_scores.get("Questions (Adapted)", "N/A"),
        "Sound Effects (Adapted)": adapted_scores.get("Sound Effects (Adapted)", "N/A"),
        "🧮 Composite Engagement Score": adapted_scores.get("Engagement Composite Score", "N/A")
    })

    # === Interpretation ===
    st.markdown("### 🗣️ Interpretation Summary")
    st.write(f"**Repetition:** {interpret_repetition_score(adapted_scores.get('Repetition (Adapted)', 0))}")
    st.write(f"**Rhyme:** {interpret_rhyme_score(adapted_scores.get('Rhyme (Adapted)', 0))}")
    st.write(f"**Questions:** {interpret_question_score(adapted_scores.get('Questions (Adapted)', 0))}")
    st.write(f"**Sound Effects:** {interpret_sound_effect_score(adapted_scores.get('Sound Effects (Adapted)', 0))}")
    st.write(f"**🧮 Composite Score:** {interpret_engagement_composite(adapted_scores.get('Engagement Composite Score', 0))}")

    # === Rubrics ===
    st.markdown("### 📘 Engagement Rubrics")
    with st.expander("🔁 Repetition"):
        st.markdown(er.repetition_rubric(), unsafe_allow_html=True)

    with st.expander("🎶 Rhyme"):
        st.markdown(er.rhyme_rubric(), unsafe_allow_html=True)

    with st.expander("❓ Questions"):
        st.markdown(er.question_rubric(), unsafe_allow_html=True)

    with st.expander("💥 Sound Effects"):
        st.markdown(er.sound_effect_rubric(), unsafe_allow_html=True)

    with st.expander("🧮 Composite Score Rubric"):
        st.markdown(er.engagement_composite_rubric(), unsafe_allow_html=True)
