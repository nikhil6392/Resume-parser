from fastapi import APIRouter, UploadFile, File
from services import extractor, matcher
from rapidfuzz import fuzz

router = APIRouter()

# 🔢 Score matching skills with fuzzy logic
def score_match(resume_skills, job_skills):
    if not job_skills:
        return 0
    matched = 0
    for job_skill in job_skills:
        for r_skill in resume_skills:
            if fuzz.token_sort_ratio(job_skill, r_skill) >= 85:
                matched += 1
                break
    return round((matched / len(job_skills)) * 100)

# 📥 POST endpoint to match resume to job descriptions
@router.post("/")
async def match_resume(
    resume: UploadFile = File(...),
    job1: UploadFile = File(...),
    job2: UploadFile = File(...)
):
    print("📥 Files uploaded")

    # 📄 Extract text
    resume_text = await extractor.extract_text_from_upload(resume)
    jd1_text = await extractor.extract_text_from_upload(job1)
    jd2_text = await extractor.extract_text_from_upload(job2)

    # 🧠 Extract skills
    resume_skills = extractor.extract_skills(resume_text)
    jd1_skills = extractor.extract_skills(jd1_text)
    jd2_skills = extractor.extract_skills(jd2_text)

    print("🧠 Resume Skills Extracted:", resume_skills)

    # 📦 Prepare job data
    jobs = [
        {
            "id": 1,
            "name": job1.filename,
            "skills": jd1_skills
        },
        {
            "id": 2,
            "name": job2.filename,
            "skills": jd2_skills
        }
    ]

    # 🔁 Add fuzzy match score to each job
    for job in jobs:
        job["score"] = score_match(resume_skills, job["skills"])
    print("📊 Jobs with scores:", jobs)

    # 🧮 Run LP to find best match
    best = matcher.optimize_best_job(jobs, resume_skills)

    # ✅ Create fresh object for frontend to re-render correctly
    if best:
        best = {
            "id": best["id"],
            "name": best["name"],
            "skills": best["skills"],
            "score": score_match(resume_skills, best["skills"])
        }
        print("🏆 Best Match Selected by LP:", best)

    return {
        "resume_skills": resume_skills,
        "jobs": jobs,
        "best_match": best
    }

