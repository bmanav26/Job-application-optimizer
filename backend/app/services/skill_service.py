from app.utils.skills import SKILLS_DB

def extract_skills(text: str):
    text = text.lower()
    found_skills = []

    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))

def calculate_match_score(resume_skills, job_skills):

    matched = list(set(resume_skills) & set(job_skills))
    missing = list(set(job_skills) - set(resume_skills))

    if len(job_skills) <= 0:
        score = 0
    else:
        score = int(len(matched)/len(job_skills)) * 100

    return score, matched, missing