import streamlit as st
import rubric.readability_rubric as rr
from rubric.interpreters.readability_interp import (
    interpret_fre_score,
    interpret_fkgl_score,
    interpret_spache_score,
    interpret_dale_chall_score,
    interpret_readability_composite
)


def render_readability_tab(cleaned_text, raw_scores, adapted_scores):
    st.subheader("📘 Readability Analysis")

    # === Cleaned Text ===
    st.markdown("### 🧼 Cleaned Text for Readability Analysis")
    st.text_area("Text Used for Analysis", cleaned_text, height=200)

    # === Raw Readability Scores ===
    st.markdown("### 📊 Standard Readability Metrics")
    st.caption("ℹ️ These are raw readability values from classic formulas.")
    st.json({
        "Flesch Reading Ease (FRE)": raw_scores.get("flesch_reading_ease", "N/A"),
        "Flesch–Kincaid Grade Level (FKGL)": raw_scores.get("flesch_kincaid_grade", "N/A"),
        "Spache Score": raw_scores.get("spache_score", "N/A"),
        "Dale–Chall Score": raw_scores.get("dale_chall_score", "N/A")
    })

    # === Adapted Developmental Scores ===
    st.markdown("### 🧠 Adapted Developmental Scores (0–1)")
    st.caption("✅ Reinterpreted to reflect how well the story matches preschool listening & language needs.")
    st.json({
        "FRE (Adapted)": adapted_scores["fre_dev"],
        "FKGL (Adapted)": adapted_scores["fkgl_dev"],
        "Spache (Adapted)": adapted_scores["spache_dev"],
        "Dale–Chall (Adapted)": adapted_scores["dale_dev"],
        "🧮 Composite Score": adapted_scores["readability_composite"]
    })

    # === Interpretations ===
    st.markdown("### 🗣️ Interpretation Summary")
    st.write(f"**Flesch Reading Ease (FRE):** {interpret_fre_score(adapted_scores['fre_dev'])}")
    st.write(f"**Flesch–Kincaid Grade Level (FKGL):** {interpret_fkgl_score(adapted_scores['fkgl_dev'])}")
    st.write(f"**Spache Score:** {interpret_spache_score(adapted_scores['spache_dev'])}")
    st.write(f"**Dale–Chall Score:** {interpret_dale_chall_score(adapted_scores['dale_dev'])}")
    st.write(f"**🧮 Composite Score:** {interpret_readability_composite(adapted_scores['readability_composite'])}")

    # === Rubrics ===
    st.markdown("### 📘 Interpretation Rubrics")

    with st.expander("🧮 Composite Readability Rubric"):
        st.markdown(rr.readability_composite_rubric(), unsafe_allow_html=True)

    with st.expander("📘 Flesch Reading Ease (FRE) Rubric"):
        st.markdown(rr.flesch_reading_ease_rubric(), unsafe_allow_html=True)

    with st.expander("📗 Flesch–Kincaid Grade Level (FKGL) Rubric"):
        st.markdown(rr.fkgl_rubric(), unsafe_allow_html=True)

    with st.expander("📙 Spache Readability Rubric"):
        st.markdown(rr.spache_rubric(), unsafe_allow_html=True)

    with st.expander("📕 Dale–Chall Readability Rubric"):
        st.markdown(rr.dale_chall_rubric(), unsafe_allow_html=True)
