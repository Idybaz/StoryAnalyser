import streamlit as st

@st.cache_resource
def get_ocr():
    # Import inside the function so the app can start even if OCR isn’t used yet
    from paddleocr import PaddleOCR
    return PaddleOCR(use_angle_cls=True, lang="en", use_gpu=False)
