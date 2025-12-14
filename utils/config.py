import platform
from paddleocr import PaddleOCR

# Detect OS and set Poppler path correctly
if platform.system() == "Windows":
    POPPLER_PATH = r"C:\Program Files\Release-24.08.0-0\poppler-24.08.0\Library\bin"
else:
    # Streamlit Cloud / Linux
    POPPLER_PATH = "/usr/bin"

# Initialize PaddleOCR once
ocr = PaddleOCR(
    use_angle_cls=True,
    lang="en",
    use_gpu=False
)
