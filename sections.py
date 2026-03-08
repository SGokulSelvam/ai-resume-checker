sections = ["education", "experience", "skills", "projects"]

def check_sections(resume_text):

    found = []

    for section in sections:
        if section in resume_text:
            found.append(section)

    return found 