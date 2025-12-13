def extract_text_from_pdf(uploaded_file, custom_pages=False, start_page=4, skip_last=1):
    import os
    import logging
    import streamlit as st
    from pdf2image import convert_from_bytes
    from utils.config import POPPLER_PATH
    from utils.ocr_loader import get_ocr
    
    ocr = get_ocr()
    uploaded_file.seek(0)

    try:
        images = convert_from_bytes(
            uploaded_file.read(),
            dpi=200,
            poppler_path=POPPLER_PATH,
            fmt='jpeg'
        )
    except Exception as e:
        logging.error(f"PDF conversion failed: {e}")
        return f"[ERROR] Could not process PDF: {e}"

    total_pages = len(images)

    # 🧼 No auto-slicing — user controls everything from app.py
    if custom_pages:
        start = max(start_page - 1, 0)
        end = total_pages - skip_last if skip_last < total_pages else total_pages
        images = images[start:end]

    extracted_text = []
    progress = st.progress(0)
    status = st.empty()

for i, image in enumerate(images, 1):
    temp_path = f"temp_page_{i}.jpg"
    try:
        image.save(temp_path, "JPEG")

        result = ocr.ocr(temp_path, cls=True) or []

        # PaddleOCR sometimes returns [None] or entries that are None
        for res in result:
            if not res:   # skips None / empty page results safely
                continue

            for line in res:
                # line is typically: [box_points, (text, score)]
                if not line or not isinstance(line, list) or len(line) < 2:
                    continue

                text_info = line[1]
                if isinstance(text_info, (list, tuple)) and len(text_info) > 0:
                    text = text_info[0]
                    if isinstance(text, str) and text.strip():
                        extracted_text.append(text)

    except Exception as e:
        logging.error(f"OCR failed on page {i}: {e}")

    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

    percent = int((i / len(images)) * 100)
    progress.progress(percent)
    status.text(f"🧠 OCR in progress: Page {i}/{len(images)} ({percent}%)")

status.text("✅ OCR complete!")
return " ".join(extracted_text) if extracted_text else "[NO TEXT FOUND]"
