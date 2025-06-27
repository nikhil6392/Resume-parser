from pulp import LpMaximize, LpProblem, LpVariable, lpSum

def optimize_best_job(jobs, resume_skills):
    model = LpProblem("Job_Match", LpMaximize)
    x = {job["id"]: LpVariable(f"x_{job['id']}", cat="Binary") for job in jobs}

    model += lpSum([x[job["id"]] * len(set(job["skills"]) & set(resume_skills)) for job in jobs])
    model += lpSum([x[job["id"]] for job in jobs]) == 1
    model.solve()

    for job in jobs:
        if x[job["id"]].value() == 1:
            return job
    return None
