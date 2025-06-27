"use client";

import React, { useState } from "react";
import { matchResumeToJobs } from "@/lib/api";

export default function FileUpload() {
  const [resume, setResume] = useState<File | null>(null);
  const [job1, setJob1] = useState<File | null>(null);
  const [job2, setJob2] = useState<File | null>(null);
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    // ✅ Safety check: All 3 files must be present
    if (!resume || !job1 || !job2) {
      alert("Please upload resume and both job descriptions.");
      return;
    }

    // ✅ Safety check: They must be valid File objects
    if (!(resume instanceof File) || !(job1 instanceof File) || !(job2 instanceof File)) {
      console.error("❌ One or more uploads are invalid File objects");
      alert("Upload error: Invalid file(s).");
      return;
    }

    console.log("📤 Submitting to API...", {
      resume: resume.name,
      job1: job1.name,
      job2: job2.name,
    });

    setLoading(true);

    try {
      const data = await matchResumeToJobs(resume, [job1, job2]);
      console.log("✅ Received match result:", data);
      setResult(data);
    } catch (err: any) {
      console.error("❌ API Error:", err?.response?.data || err?.message || err);
      alert("Something went wrong. Check browser console.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-6 space-y-4 max-w-xl mx-auto">
      <h1 className="text-2xl font-bold">Resume Matcher</h1>

      <div className="space-y-2">
        <label className="block font-medium">Upload Resume (.pdf or .docx)</label>
        <input
          type="file"
          accept=".pdf,.docx"
          onChange={(e) => setResume(e.target.files?.[0] || null)}
        />
      </div>

      <div className="space-y-2">
        <label className="block font-medium">Upload Job Description 1 (.txt)</label>
        <input
          type="file"
          accept=".txt"
          onChange={(e) => setJob1(e.target.files?.[0] || null)}
        />
      </div>

      <div className="space-y-2">
        <label className="block font-medium">Upload Job Description 2 (.txt)</label>
        <input
          type="file"
          accept=".txt"
          onChange={(e) => setJob2(e.target.files?.[0] || null)}
        />
      </div>

      <button
        onClick={handleSubmit}
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        disabled={loading}
      >
        {loading ? "Matching..." : "Match Jobs"}
      </button>

      {result && (
        <div className="mt-4 p-4 bg-gray-100 rounded shadow">
          <h2 className="font-semibold">Resume Skills</h2>
          <p>{result.resume_skills?.join(", ") || "No skills extracted"}</p>

          <h2 className="mt-2 font-semibold">Best Match</h2>
          <p>{result.best_match?.name || "No match found"}</p>

          <h2 className="mt-2 font-semibold">Job Required Skills:</h2>
          <p>{result.best_match?.skills?.join(", ") || "None listed"}</p>
        </div>
      )}
    </div>
  );
}
