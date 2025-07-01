from pulp import LpMaximize, LpProblem, LpVariable, lpSum, PULP_CBC_CMD

def optimize_best_job(jobs, resume_skills):
    print("🧠 optimize_best_job() CALLED")
    print("📄 Resume Skills:", resume_skills)

    model = LpProblem("Job_Match", LpMaximize)
    x = {job["id"]: LpVariable(f"x_{job['id']}", cat="Binary") for job in jobs}

    # Calculate matching score (overlap count)
    match_scores = {job["id"]: len(set(job["skills"]) & set(resume_skills)) for job in jobs}
    print("🎯 Match scores (overlaps):", match_scores)

    # Objective: Maximize total skill match
    model += lpSum(x[job_id] * score for job_id, score in match_scores.items())

    # Constraint: only one job can be selected
    model += lpSum(x.values()) == 1

    # Solve
    model.solve(PULP_CBC_CMD(msg=True))

    for job in jobs:
        if x[job["id"]].value() == 1:
            print("🏆 LP selected job:", job["name"])
            return job

    print("⚠️ LP did not select any job")
    return None
