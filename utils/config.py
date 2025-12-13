from paddleocr import PaddleOCR

# Make sure this matches your local Poppler installation path
POPPLER_PATH = None

# Initialize PaddleOCR once
ocr = PaddleOCR(use_angle_cls=True, lang="en", use_gpu=False)  # Set use_gpu=True if available
