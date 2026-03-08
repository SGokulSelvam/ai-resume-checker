def generate_suggestions(score, missing_keywords, sections_found):

    suggestions = []

    if score < 60:
        suggestions.append("Add more keywords from the job description.")

    if len(missing_keywords) > 5:
        suggestions.append("Your resume is missing many important keywords.")

    if "projects" not in sections_found:
        suggestions.append("Add a Projects section to highlight practical experience.")

    if "skills" not in sections_found:
        suggestions.append("Include a clear technical skills section.")

    suggestions.append("Add measurable achievements with numbers.")

    return suggestions