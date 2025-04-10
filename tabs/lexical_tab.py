import streamlit as st
import rubric.lexical_rubric as lr
from rubric.interpreters.lexical_interp import (
    interpret_ttr_score,
    interpret_mattr_score,
    interpret_mtld_score,
    interpret_hdd_score,
    interpret_lexical_composite
)


def render_lexical_tab(cleaned_text, raw_scores, adapted_scores):
    st.subheader("🧠 Lexical Diversity")

    # === Cleaned Text ===
    st.markdown("### 🧹 Cleaned Text for Lexical Analysis")
    st.text_area("Lexical Cleaned Text", cleaned_text, height=200)

    # === Handle Short Input ===
    if "error" in raw_scores:
        st.warning("📉 Text too short for reliable lexical diversity metrics.")
        return

    # === Raw Scores ===
    st.markdown("### 📊 Raw Lexical Diversity Metrics")
    st.json({
        "TTR": raw_scores.get("ttr", "N/A"),
        "MATTR": raw_scores.get("mattr", "N/A"),
        "MTLD": raw_scores.get("mtld", "N/A"),
        "HDD": raw_scores.get("hdd", "N/A"),
    })
    st.caption("ℹ️ TTR can be inflated in short texts. Prefer MATTR, MTLD, or HDD for more stable estimates.")

    # === Adapted Scores ===
    st.markdown("### 🧠 Adapted Lexical Diversity Scores (0–1)")
    st.caption("✅ Reflects vocabulary richness appropriate for early learners.")
    st.json({
        "TTR (Adapted)": adapted_scores["TTR (Adapted)"],
        "MATTR (Adapted)": adapted_scores["MATTR (Adapted)"],
        "MTLD (Adapted)": adapted_scores["MTLD (Adapted)"],
        "HDD (Adapted)": adapted_scores["HDD (Adapted)"],
        "🧮 Composite Score": adapted_scores["lexical_composite"]
    })

    # === Interpretations ===
    st.markdown("### 🗣️ Interpretation Summary")
    st.write(f"**TTR:** {interpret_ttr_score(adapted_scores['TTR (Adapted)'])}")
    st.write(f"**MATTR:** {interpret_mattr_score(adapted_scores['MATTR (Adapted)'])}")
    st.write(f"**MTLD:** {interpret_mtld_score(adapted_scores['MTLD (Adapted)'])}")
    st.write(f"**HDD:** {interpret_hdd_score(adapted_scores['HDD (Adapted)'])}")
    st.write(f"**🧮 Composite Score:** {interpret_lexical_composite(adapted_scores['lexical_composite'])}")

    # === Rubrics ===
    st.markdown("### 📘 Lexical Diversity Rubrics")

    with st.expander("🧮 Composite Lexical Rubric"):
        st.markdown(lr.lexical_composite_rubric(), unsafe_allow_html=True)

    with st.expander("🔠 TTR Rubric"):
        st.markdown(lr.ttr_rubric(), unsafe_allow_html=True)

    with st.expander("📈 MATTR Rubric"):
        st.markdown(lr.mattr_rubric(), unsafe_allow_html=True)

    with st.expander("🔡 MTLD Rubric"):
        st.markdown(lr.mtld_rubric(), unsafe_allow_html=True)

    with st.expander("🔢 HDD Rubric"):
        st.markdown(lr.hdd_rubric(), unsafe_allow_html=True)
