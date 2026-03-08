def keyword_analysis(resume_text, job_description):

    jd_words = set(job_description.lower().split())
    resume_words = set(resume_text.split())

    matched = jd_words.intersection(resume_words)
    missing = jd_words.difference(resume_words)

    return list(matched)[:20], list(missing)[:20]