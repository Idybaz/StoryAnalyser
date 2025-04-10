import streamlit as st
import pandas as pd
import rubric.eyfs_rubric as ey
from rubric.interpreters.eyfs_interp import interpret_main_theme, interpret_top_themes

def render_eyfs_tab(original_text, main_theme, score_dict):
    st.subheader("🌱 EYFS Alignment & Thematic Insights")

    # === Story Text
    st.markdown("### 📄 Story Text (Used for Theme Matching)")
    st.text_area("Original Text", original_text, height=200)

    # === Main Theme
    st.markdown("### 🏆 Most Relevant EYFS Theme")
    if main_theme:
        st.success(f"**{main_theme}**")
        st.info(interpret_main_theme(main_theme))
    else:
        st.warning("⚠️ No dominant theme found.")

    # === Top 3 Themes
    st.markdown("### 📌 Top 3 Matching Themes")
    top_3 = sorted(score_dict.items(), key=lambda x: x[1], reverse=True)[:3]
    for theme, score in top_3:
        st.markdown(f"- **{theme}** — *{round(score, 3)}*")

    # === Interpretation Summary
    st.markdown("### 🗣️ EYFS Alignment Interpretation")
    st.markdown(interpret_top_themes(score_dict))

    # === Expandable Full Table
    st.markdown("### 📊 View All EYFS Theme Scores")
    with st.expander("🔽 Expand Full EYFS Theme Table"):
        df = pd.DataFrame(sorted(score_dict.items(), key=lambda x: x[1], reverse=True),
                          columns=["EYFS Theme", "Similarity Score"])
        df["Similarity Score"] = df["Similarity Score"].round(3)
        st.dataframe(df, use_container_width=True)

    # === Rubric
    st.markdown("### 📘 EYFS Thematic Rubric")
    with st.expander("📘 How to Interpret Theme Scores"):
        st.markdown(ey.eyfs_similarity_rubric(), unsafe_allow_html=True)
