def interpret_main_theme(theme: str) -> str:
    if not theme:
        return "❌ No main EYFS theme detected."
    return f"🏆 This book most strongly aligns with **{theme}**, suggesting it's well-suited to promote this developmental area."

def interpret_top_themes(theme_scores: dict) -> str:
    themes = sorted(theme_scores.items(), key=lambda x: x[1], reverse=True)[:3]
    insights = []
    for label, score in themes:
        if score >= 0.3:
            insights.append(f"✅ **{label}** — Strong match (Score: {round(score, 2)})")
        elif score >= 0.2:
            insights.append(f"⚠️ **{label}** — Partial alignment (Score: {round(score, 2)})")
        else:
            insights.append(f"❌ **{label}** — Weak match (Score: {round(score, 2)})")
    return "\n".join(insights) if insights else "❌ No strong EYFS themes identified."
