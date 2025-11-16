from typing import Dict, Any
import time

JOBS: Dict[str, Dict[str, Any]] = {}

def create_job(requirement: Dict) -> str:
    job_id = f"job_{int(time.time()*1000)}"
    JOBS[job_id] = {
        "id": job_id,
        "requirement": requirement,
        "status": "queued",
        "testcases": [],
        "created_at": time.time()
    }
    return job_id

def update_job(job_id: str, **kwargs):
    if job_id not in JOBS:
        return False
    JOBS[job_id].update(kwargs)
    return True

def get_job(job_id: str):
    return JOBS.get(job_id)

def list_jobs():
    return list(JOBS.keys())
