from fastapi import APIRouter, UploadFile, File, Form
from app.services.skill_service import extract_skills, calculate_match_score
import fitz

router = APIRouter()

@router.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    pdf_bytes = await resume.read()
    pdf = fitz.open(stream=pdf_bytes, filetype="pdf")

    resume_text = ""

    for page in pdf:
        resume_text += page.get_text()

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    score, matched, missing = calculate_match_score(resume_skills, job_skills)

    return {
        "message": "Resume processed successfully",
        "score": score,
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "matched_skills": matched,
        "missing_skills": missing
    }