from nlp import extract_features
from generator import generate_testcases
from jobs import create_job, update_job, get_job
from exporter import export_csv, export_pdf
import time

class Orchestrator:
    def __init__(self):
        pass

    def submit_requirement(self, req: dict) -> str:
        job_id = create_job(req)
        update_job(job_id, status='processing')
        features = extract_features(req['raw_text'])
        update_job(job_id, status='analyzed', analysis=features)
        testcases = generate_testcases(job_id, features)
        update_job(job_id, status='generated', testcases=testcases)
        update_job(job_id, status='completed', completed_at=time.time())
        return job_id

    def get_job_status(self, job_id: str):
        return get_job(job_id)

    def get_testcases_for_job(self, job_id: str):
        j = get_job(job_id)
        if not j:
            return None
        return j.get('testcases', [])

    def export_job(self, job_id: str, format: str = 'csv'):
        j = get_job(job_id)
        if not j:
            return None
        req = j['requirement']
        tcs = j.get('testcases', [])
        if format == 'csv':
            path = export_csv(job_id, tcs)
        else:
            path = export_pdf(job_id, req, tcs)
        return {"file": path}
