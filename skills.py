skills_list = [
    "python","machine learning","deep learning",
    "sql","pandas","numpy","tensorflow",
    "pytorch","nlp","data analysis","scikit-learn"
]

def detect_skills(resume_text):

    found_skills = []

    for skill in skills_list:
        if skill in resume_text:
            found_skills.append(skill)

    return found_skills