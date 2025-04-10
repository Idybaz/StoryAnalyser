import streamlit as st
from extractor.pdf_extractor import extract_text_from_pdf
from utils.cleaner_base import preclean_text

# === Page Setup ===
st.set_page_config(page_title="📤 Upload Story", layout="centered")
st.title("📤 Upload a Storybook")
st.markdown("Upload a PDF, TXT file, or paste the story content. Then go to **Analysis Results** to explore insights.")

# === Book Title ===
book_title = st.text_input("📚 Book Title", placeholder="e.g. The Duck Who Didn’t Like Water")

# === Info box ===
st.info("📌 **Upload only the story content.**\n"
        "If your file contains extra pages (title, copyright, reviews), "
        "use the trim options below.")

# === Input Method ===
story_source = st.radio("Choose Input Method:", ["Upload PDF", "Upload TXT", "Paste Text"])
extracted_text = ""
uploaded_file = None
custom_pages = False
start_page = 1
skip_last = 0

# === Handle Upload Options ===
if story_source == "Upload PDF":
    uploaded_file = st.file_uploader("📂 Upload a PDF", type=["pdf"])
    if uploaded_file:
        custom_pages = st.checkbox("✂️ Trim PDF pages?", value=False)
        if custom_pages:
            start_page = st.number_input("Start from page", min_value=1, value=1)
            skip_last = st.number_input("Skip pages from end", min_value=0, value=0)

elif story_source == "Upload TXT":
    uploaded_file = st.file_uploader("📄 Upload a TXT file", type=["txt"])
    if uploaded_file:
        lines = uploaded_file.read().decode("utf-8").splitlines()
        total_lines = len(lines)
        custom_pages = st.checkbox("✂️ Trim TXT lines?", value=False)
        if custom_pages:
            start = st.number_input("Start from line", min_value=1, max_value=total_lines, value=1)
            skip = st.number_input("Skip lines from end", min_value=0, max_value=total_lines, value=0)
            extracted_text = "\n".join(lines[start-1:total_lines - skip])
        else:
            extracted_text = "\n".join(lines)

elif story_source == "Paste Text":
    extracted_text = st.text_area("✍️ Paste your story here", height=300)

# === Process Story Button ===
if st.button("🚀 Process Story"):
    if not book_title.strip():
        st.warning("⚠️ Please enter a book title.")
    elif story_source != "Paste Text" and not uploaded_file:
        st.warning("⚠️ Please upload your file.")
    elif story_source == "Paste Text" and not extracted_text.strip():
        st.warning("⚠️ Please paste your story.")
    else:
        if story_source == "Upload PDF" and uploaded_file:
            with st.spinner("⏳ Extracting text from PDF..."):
                extracted_text = extract_text_from_pdf(
                    uploaded_file,
                    custom_pages=custom_pages,
                    start_page=start_page,
                    skip_last=skip_last
                )

        if extracted_text and not extracted_text.startswith("[ERROR]"):
            st.success("✅ Story processed!")

            precleaned = preclean_text(extracted_text)

            # Save to session state
            st.session_state["book_title"] = book_title.strip()
            st.session_state["extracted_text"] = extracted_text
            st.session_state["precleaned"] = precleaned
            st.session_state["story_processed"] = True  # ✅ set flag for showing Analyze button

            st.text_area("📜 Extracted Text Preview", extracted_text, height=300)
        else:
            st.error("⚠️ Text extraction failed.")

# === Analyze Now Button (only show after processing) ===
if st.session_state.get("story_processed"):
    if st.button("🔎 Analyze Now"):
        st.switch_page("pages/2_Analysis_Results.py")
