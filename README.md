# 🧠 Resume Matcher using Linear Programming

Resume Matcher is an intelligent job-matching engine that uses **Linear Programming (PuLP)** to optimize candidate-job fit based on **maximum skill overlap**. It allows users to upload multiple job descriptions and compares them with a resume to suggest the best-fitting roles.

## 🚀 Features

- 🔍 Match a single resume against multiple job descriptions
- 📊 Score each job description based on skill relevance and overlap
- 🧠 Uses **Linear Programming** for optimal selection
- ⚙️ Backend built with **FastAPI**
- 🌐 Frontend with **Next.js** and **Tailwind CSS**
- 🔐 Optional authentication with **AWS OIDC** 

## 📚 Tech Stack

- **Frontend**: Next.js, Tailwind CSS
- **Backend**: FastAPI, Python
- **Optimization Engine**: PuLP (Linear Programming)
- **Authentication**: AWS Cognito / OIDC (optional)
- **Deployment**: AWS (EC2/S3 planned)


## ⚡ How It Works

1. User uploads a resume (PDF/Text)
2. User uploads one or more job descriptions
3. The system parses and extracts keywords/skills
4. A linear programming model is formulated to match based on skill overlap
5. Ranks all job descriptions and returns the best match(es)

## 🧪 Example

- **Input**: Resume with skills `[Python, FastAPI, LP, NLP]`
- **JDs**: 
   - JD 1: `[JavaScript, React, Node.js]`
   - JD 2: `[Python, FastAPI, Optimization]`
- **Output**: JD 2 matched with 75% skill overlap score

## 🛠️ Getting Started

### Backend (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload

cd frontend
npm install
npm run dev

```

Let me know if you'd like:
- A badge section (e.g. GitHub stars, license)
- Deployment instructions (e.g. for AWS or Docker)
- Screenshots or demo GIFs added


📈 Future Improvements
Resume parsing using NLP (spaCy / BERT)

JD clustering and job taxonomy analysis

Scoring explainability and skill weighting

Resume feedback and improvement suggestions

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

📄 License
MIT

🧑‍💻 Author
Built by [Nikhil pathak] – developerop.vercel.app
Contact: nikhilpathak210431@email.com
