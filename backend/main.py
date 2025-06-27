from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import match

app = FastAPI(title="Resume Extractor")

# Add CORS settings here
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(match.router, prefix="/match", tags=["Match"])

@app.get("/")
def root():
    return {"message": "Welcome to the Resume Matcher API!"}