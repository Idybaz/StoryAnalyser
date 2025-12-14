import os
import platform
import streamlit as st
from paddleocr import PaddleOCR

def get_poppler_path():
    # On Streamlit Cloud (Linux), poppler-utils installs binaries in PATH already.
    if platform.system() != "Windows":
        return None

    # Windows local dev: set this to your real Poppler bin folder
    return os.getenv(
        "POPPLER_PATH",
        r"C:\Program Files\Release-24.08.0-0\poppler-24.08.0\Library\bin"
    )

@st.cache_resource
def get_ocr():
    # show_log=False reduces noisy logs and startup overhead
    return PaddleOCR(use_angle_cls=True, lang="en", use_gpu=False, show_log=False)
