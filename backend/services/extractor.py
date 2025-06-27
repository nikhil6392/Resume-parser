import re
from pdfminer.high_level import extract_text as extract_pdf
from docx import Document
from fastapi import UploadFile

SKILLS = ["python", "java", "sql", "docker", "aws", "react", "excel", "nlp", "git"]

async def extract_text_from_upload(file: UploadFile):
    content = await file.read()
    path = f"/temp/file.filename"
    with open(path, "wb") as f:
        f.write(content)

    if file.filename.endswith(".pdf"):
        return extract_pdf(path)
    elif file.filename.endswith(".docx"):
        return "/n".join(p.text for p in Document(path).paragraphs)
    elif file.filename.endswith(".txt"):
        return content.decode("utf-8")
    return ""

def extract_skills(text):
    return [s for s in SKILLS if re.search(rf"\b{s}\b", text, re.IGNORECASE)]
