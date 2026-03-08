skills_list = [
    "python",
    "machine learning",
    "deep learning",
    "sql",
    "pandas",
    "numpy",
    "tensorflow",
    "pytorch",
    "nlp",
    "data analysis",
    "scikit-learn",
    "aws",
    "docker",
    "kubernetes",
    "power bi",
    "tableau"
]


def detect_skills(resume_text):

    found = []

    for skill in skills_list:
        if skill in resume_text:
            found.append(skill)

    return found


def missing_skills(resume_text, job_description):

    required = []

    for skill in skills_list:
        if skill in job_description.lower():
            required.append(skill)

    missing = []

    for skill in required:
        if skill not in resume_text:
            missing.append(skill)

    return missing