from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from orchestrator import Orchestrator
import os

app = FastAPI(title="Quality Guardian - Prototype")

os.makedirs("exports", exist_ok=True)

orch = Orchestrator()

class RequirementIn(BaseModel):
    title: str
    module: str = "default"
    raw_text: str

@app.post("/requirements")
async def submit_requirement(req: RequirementIn):
    job_id = orch.submit_requirement(req.dict())
    return {"job_id": job_id, "status": "submitted"}

@app.get("/jobs/{job_id}")
async def job_status(job_id: str):
    status = orch.get_job_status(job_id)
    if not status:
        raise HTTPException(status_code=404, detail="Job not found")
    return status

@app.get("/jobs/{job_id}/testcases")
async def get_testcases(job_id: str):
    items = orch.get_testcases_for_job(job_id)
    if items is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return {"testcases": items}

@app.post("/jobs/{job_id}/export")
async def export_job(job_id: str, format: str = "csv"):
    out = orch.export_job(job_id, format=format)
    if not out:
        raise HTTPException(status_code=404, detail="Job not found or nothing to export")
    return out
