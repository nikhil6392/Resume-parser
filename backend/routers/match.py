from fastapi import APIRouter, UploadFile, File
from services import extractor, matcher

router = APIRouter()

@router.post("/")
async def match_resume(resume: UploadFile = File(...), job1: UploadFile = File(...), job2: UploadFile = File(...)):
    resume_text = await extractor.extract_text_from_upload(resume)
    jd1_text = await extractor.extract_text_from_upload(job1)
    jd2_text = await extractor.extract_text_from_upload(job2)

    resume_skills = extractor.extract_skills(resume_text)
    jobs = [
        {"id": 1, "name": job1.filename, "skills": extractor.extract_skills(jd1_text)},
        {"id": 2, "name": job2.filename, "skills": extractor.extract_skills(jd2_text)}
    ]

    best = matcher.optimize_best_job(jobs, resume_skills)
    return {
        "resume_skills": resume_skills,
        "best_match": best
    }