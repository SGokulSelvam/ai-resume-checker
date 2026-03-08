def explain_match(score):

    if score >= 80:
        return "Your resume strongly matches the job description."

    elif score >= 60:
        return "Your resume partially matches the job requirements."

    elif score >= 40:
        return "Your resume has limited match with the job description."

    else:
        return "Your resume is poorly aligned with the job description."