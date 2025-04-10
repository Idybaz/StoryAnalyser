# app/analysis/normalized/readability.py

def normalize_fre(fre_score):
    if fre_score >= 90:
        return 1.0
    elif fre_score >= 85:
        return 0.9
    elif fre_score >= 80:
        return 0.8
    elif fre_score >= 75:
        return 0.6
    elif fre_score >= 70:
        return 0.4
    else:
        return 0.2

def normalize_fkgl(fkgl_score):
    if fkgl_score <= 1.0:
        return 1.0
    elif fkgl_score <= 1.5:
        return 0.9
    elif fkgl_score <= 2.0:
        return 0.8
    elif fkgl_score <= 2.5:
        return 0.6
    elif fkgl_score <= 3.0:
        return 0.4
    else:
        return 0.2

def normalize_spache(spache_score):
    if spache_score <= 1.0:
        return 1.0
    elif spache_score <= 1.5:
        return 0.9
    elif spache_score <= 2.0:
        return 0.8
    elif spache_score <= 2.5:
        return 0.6
    elif spache_score <= 3.0:
        return 0.4
    else:
        return 0.2

def normalize_dale(dale_score):
    if dale_score <= 4.9:
        return 1.0
    elif dale_score <= 5.5:
        return 0.9
    elif dale_score <= 6.0:
        return 0.8
    elif dale_score <= 6.5:
        return 0.6
    elif dale_score <= 7.0:
        return 0.4
    else:
        return 0.2


def normalize_readability_scores(raw_scores: dict) -> dict:
    fre = normalize_fre(raw_scores.get("flesch_reading_ease", 0))
    fkgl = normalize_fkgl(raw_scores.get("flesch_kincaid_grade", 99))
    spache = normalize_spache(raw_scores.get("spache_score", 99))
    dale = normalize_dale(raw_scores.get("dale_chall_score", 99))

    composite = round((fre + fkgl + spache + dale) / 4, 3)

    return {
        "fre_dev": fre,
        "fkgl_dev": fkgl,
        "spache_dev": spache,
        "dale_dev": dale,
        "readability_composite": composite
    }

