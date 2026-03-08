import pandas as pd

def create_report(score, skills, matched, missing, suggestions):

    data = {
        "ATS Score":[score],
        "Skills Found":[", ".join(skills)],
        "Matched Keywords":[", ".join(matched)],
        "Missing Keywords":[", ".join(missing)],
        "Suggestions":[", ".join(suggestions)]
    }

    df = pd.DataFrame(data)

    return df