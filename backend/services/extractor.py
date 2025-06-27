import os
import re
from pdfminer.high_level import extract_text as extract_pdf
from docx import Document
from fastapi import UploadFile

UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "..", "uploads")

SKILLS = ["python", "java", "sql", "docker", "aws", "react", "excel", "nlp", "git"]

# This function saves the uploaded file and extracts text from it
async def extract_text_from_upload(file: UploadFile) -> str:
    #  Make sure the uploads directory exists
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    #  Create full file path like 'backend/uploads/resume.pdf'
    path = os.path.join(UPLOAD_DIR, file.filename)

    #  Save the uploaded file
    content = await file.read()
    with open(path, "wb") as f:
        f.write(content)

    #  Extract text based on file extension
    if file.filename.endswith(".pdf"):
        return extract_pdf(path)
    elif file.filename.endswith(".docx"):
        return "\n".join(p.text for p in Document(path).paragraphs)
    elif file.filename.endswith(".txt"):
        return content.decode("utf-8")
    return ""

#  Skill matcher using regex
def extract_skills(text: str):
    return [s for s in SKILLS if re.search(rf"\b{s}\b", text, re.IGNORECASE)]
