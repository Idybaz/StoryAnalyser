def interpret_top_words(top_words: list) -> str:
    if not top_words:
        return "❌ No frequent words detected — text may be too short or inconsistent."
    return f"🧠 Main focus: {', '.join([word for word, _ in top_words[:3]])}"

def interpret_keybert_phrases(keywords: list) -> str:
    if not keywords:
        return "❌ No strong themes detected. Try increasing story length or clarity."
    
    top = keywords[0][0]
    return f"💡 Most salient theme: **{top}** — reflects central idea or character."
