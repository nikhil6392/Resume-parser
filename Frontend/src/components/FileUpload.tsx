"use client"

import React ,{ useState } from "react";
import { matchResumeToJobs } from "@/lib/api";

export default function FileUpload(){
    const [resume, setResume] = useState<File | null>(null);
    const [jobs, setJobs] = useState<File[]>([]);
    const [result, setResult] = useState<any>(null);
    const [loading, setLoading] = useState(false);

    const handleSubmit = async () => {
        if (!resume || jobs.length === 0) return alert("Upload both resume and jobs")

        setLoading(true);
        try {
            const data = await matchResumeToJobs(resume, jobs.slice(0, 2));
            setResult(data);
        } catch(err){
            alert("Error matching resume")
        }finally {
            setLoading(false)
        }
    }

    return (
        <div className="">
            <h1>Resume Matcher</h1>

            <input type="file" accept=".pdf,.docx" onChange={(e) => setResume(e.target.files?.[0] || null)} />
            <input type="file" accept=".txt" multiple onChange={(e) => setJobs(Array.from(e.target.files || []))} />

            <button 
                onClick={handleSubmit}
                className=""
                disabled={loading}
            >
                {loading ? "Matching..." : "Match Jobs"}
            </button>

            {result && (
                <div>
                    <h2>Resume Skills</h2>
                    <p>{result.resume_skills.join(", ")}</p>

                    <h2>Best Match</h2>
                    <p>{result.best_match.name}</p>

                    <h2>Job Required Skills:</h2>
                    <p>{result.best_match.skills.join(", ")}</p>
                </div>
            )}
        </div>
    )
}