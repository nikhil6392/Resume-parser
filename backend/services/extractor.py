import os
import re
import json
from pdfminer.high_level import extract_text as extract_pdf
from docx import Document
from fastapi import UploadFile

# Create platform-independent paths
BASE_DIR = os.path.dirname(__file__)
UPLOAD_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "uploads"))
SKILL_FILE = os.path.join(BASE_DIR, "skills.txt")
SYNONYM_FILE = os.path.join(BASE_DIR, "skill_synonyms.json")

# Create uploads directory if it doesn't exist
os.makedirs(UPLOAD_DIR, exist_ok=True)

# 🧠 Extract text from uploaded files
async def extract_text_from_upload(file: UploadFile) -> str:
    path = os.path.join(UPLOAD_DIR, file.filename)

    content = await file.read()
    with open(path, "wb") as f:
        f.write(content)

    if file.filename.endswith(".pdf"):
        return extract_pdf(path)
    elif file.filename.endswith(".docx"):
        return "\n".join(p.text for p in Document(path).paragraphs)
    elif file.filename.endswith(".txt"):
        return content.decode("utf-8")
    return ""

# 🧽 Normalize text for skill matching
def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s\+\-#]", " ", text)
    return re.sub(r"\s+", " ", text)

# 📥 Load known skills
def load_skills() -> list:
    with open(SKILL_FILE, "r", encoding="utf-8") as f:
        return [line.strip().lower() for line in f.readlines()]

# 🔄 Load synonyms like js → javascript
def load_synonyms() -> dict:
    try:
        with open(SYNONYM_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# 🔍 Extract matched skills from resume text
def extract_skills(text: str) -> list:
    text = clean_text(text)
    skills = load_skills()
    synonyms = load_synonyms()
    found = set()

    for skill in skills:
        if re.search(rf"\b{re.escape(skill)}\b", text):
            found.add(skill)

    for word in text.split():
        if word in synonyms:
            found.add(synonyms[word])

    return sorted(found)
