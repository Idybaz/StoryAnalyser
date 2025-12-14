def extract_text_from_pdf(uploaded_file, custom_pages=False, start_page=4, skip_last=1):
    import logging
    import streamlit as st
    import numpy as np
    from pdf2image import convert_from_bytes
    from utils.config import get_poppler_path, get_ocr

    poppler_path = get_poppler_path()
    ocr = get_ocr()

    uploaded_file.seek(0)

    try:
        images = convert_from_bytes(
            uploaded_file.read(),
            dpi=200,
            poppler_path=poppler_path,
            fmt="jpeg"
        )
    except Exception as e:
        logging.error(f"PDF conversion failed: {e}")
        return f"[ERROR] Could not process PDF: {e}"

    total_pages = len(images)

    if custom_pages:
        start = max(start_page - 1, 0)
        end = total_pages - skip_last if skip_last < total_pages else total_pages
        images = images[start:end]

    extracted_text = []
    progress = st.progress(0)
    status = st.empty()

    for i, image in enumerate(images, 1):
        try:
            img = np.array(image)
            result = ocr.ocr(img, cls=True)

            if result:
                for res in result:
                    for line in res:
                        if line and isinstance(line, list) and len(line) > 1:
                            text = line[1][0]
                            if isinstance(text, str):
                                extracted_text.append(text)

        except Exception as e:
            logging.error(f"OCR failed on page {i}: {e}")

        percent = int((i / len(images)) * 100)
        progress.progress(percent)
        status.text(f"🧠 OCR in progress: Page {i}/{len(images)} ({percent}%)")

    status.text("✅ OCR complete!")
    return " ".join(extracted_text) if extracted_text else "[NO TEXT FOUND]"
