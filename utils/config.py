import platform
from paddleocr import PaddleOCR

# Poppler path: Windows vs Streamlit Cloud/Linux
POPPLER_PATH = (
    r"C:\Program Files\Release-24.08.0-0\poppler-24.08.0\Library\bin"
    if platform.system() == "Windows"
    else "/usr/bin"
)

@st.cache_resource
def get_ocr():
    # show_log=False reduces noisy debug logs
    return PaddleOCR(use_angle_cls=True, lang="en", use_gpu=False, show_log=False)
