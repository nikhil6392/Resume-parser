from fastapi import FastAPI
from routers import match

app = FastAPI(title="Resume Extractor")

app.include_router(match.router, prefix="/match", tags=["Match"])

@app.get("/")
def root():
    return {"message": "Welcome to the Resume Matcher API!"}