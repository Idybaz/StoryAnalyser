import streamlit as st

st.set_page_config(page_title="📖 Story Analyzer", layout="centered")

st.title("📖 Welcome to the Interactive Story Analyzer!")
st.markdown("Upload and analyze children's storybooks for style, tone, and structure.")

if st.button("🚀 Upload a Story"):
    st.session_state["go_to_upload"] = True

# Redirect logic
if st.session_state.get("go_to_upload"):
    st.session_state["go_to_upload"] = False  # Reset after navigation
    st.switch_page("pages/1_Upload_Story.py")  # This works in Streamlit ≥1.18.0+
