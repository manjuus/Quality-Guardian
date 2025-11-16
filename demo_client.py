import requests
import json
import time

BASE = "http://localhost:8000"

sample = {
    "title": "User Login",
    "module": "Auth",
    "raw_text": "As a registered user, I should be able to login with email and password so that I can access my dashboard. The system should show an error message for invalid credentials."
}

resp = requests.post(f"{BASE}/requirements", json=sample)
print("Submit response:", resp.json())
job_id = resp.json().get('job_id')

for _ in range(10):
    time.sleep(1)
    s = requests.get(f"{BASE}/jobs/{job_id}")
    print(s.json())
    if s.json().get('status') == 'completed':
        break

r = requests.get(f"{BASE}/jobs/{job_id}/testcases")
print("Generated testcases:")
print(json.dumps(r.json(), indent=2))

ex = requests.post(f"{BASE}/jobs/{job_id}/export", params={"format":"csv"})
print("Export:", ex.json())
print("Check backend/exports for files.")
