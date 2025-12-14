import os
import platform
import streamlit as st
from paddleocr import PaddleOCR


def get_poppler_path():
    """
    pdf2image:
    - On Streamlit Cloud (Linux): poppler-utils is installed via packages.txt, so PATH is fine → return None.
    - On Windows: must point to Poppler /bin.
    - On Linux local dev (optional): allow POPPLER_PATH override if you set it.
    """
    system = platform.system()

    if system == "Windows":
        return os.getenv(
            "POPPLER_PATH",
            r"C:\Program Files\Release-24.08.0-0\poppler-24.08.0\Library\bin"
        )

    # Linux/macOS: usually not needed; but allow override if you set POPPLER_PATH
    return os.getenv("POPPLER_PATH") or None


@st.cache_resource(show_spinner=False)
def get_ocr():
    # show_log=False reduces noisy logs and startup overhead
    return PaddleOCR(use_angle_cls=True, lang="en", use_gpu=False, show_log=False)
