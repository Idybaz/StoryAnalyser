import os
import streamlit as st

@st.cache_resource(show_spinner=False)
def get_spacy():
    import spacy
    return spacy.load("en_core_web_sm")

@st.cache_resource(show_spinner=False)
def get_paddle_ocr():
    from paddleocr import PaddleOCR
    return PaddleOCR(use_angle_cls=True, lang="en", use_gpu=False, show_log=False)

@st.cache_resource(show_spinner=False)
def get_sentence_transformer():
    from sentence_transformers import SentenceTransformer
    return SentenceTransformer("all-MiniLM-L6-v2")

@st.cache_resource(show_spinner=False)
def get_keybert():
    from keybert import KeyBERT
    return KeyBERT("all-MiniLM-L6-v2")

@st.cache_resource(show_spinner=False)
def get_emotion_pipeline():
    # Make sure HF caches are used
    os.environ.setdefault("HF_HOME", "/home/appuser/.cache/huggingface")
    from transformers import pipeline
    return pipeline(
        "text-classification",
        model="j-hartmann/emotion-english-distilroberta-base",
        return_all_scores=True
    )
