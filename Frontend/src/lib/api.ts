import axios from 'axios';

const API_BASE = "http://localhost:8000";

export const matchResumeToJobs = async (resume: File, jobs: File[]) => {
  if (jobs.length < 2) {
    throw new Error("Please upload exactly 2 job description files.");
  }

  const formData = new FormData();
  formData.append("resume", resume);
  formData.append("job1", jobs[0]);
  formData.append("job2", jobs[1]);

  const response = await axios.post(`${API_BASE}/match/`, formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
    validateStatus: () => true,
  });

  if (response.status !== 200) {
    throw new Error("Non-200 response from API");
  }

  return response.data;
};

