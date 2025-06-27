import axios from 'axios'

const API_BASE = "http://localhost:8000";

export const matchResumeToJobs = async (resume: File, jobs: File[]) => {
    const formData = new FormData();
    formData.append("resume", resume);
    jobs.forEach((job, i) => {
        formData.append(`job${i + 1}` , job);
    });

    const response = await axios.post(`${API_BASE}/match/`, formData, {
        headers: {
            "Content-Type": "multipart/form-data",
        }
    })

    return response.data;
}