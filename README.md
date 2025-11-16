# Quality Guardian

**Enterprise Release Quality Guardian — Multi-Agent QA Automation**

Quality Guardian is an AI-powered multi-agent framework (FastAPI backend + React dashboard) that automates requirement analysis, test-case generation, coverage checks and release-quality scoring for enterprise software projects. This repository contains a runnable prototype, clear architecture, and instructions to extend it into a production-ready system.

---

## Quick Start (Local)

1. Create and activate a Python virtual environment (Python 3.10+).
2. Install dependencies: `pip install -r requirements.txt`
3. Start the backend: `cd backend && uvicorn app:app --reload --port 8000`
4. Run the demo client from the repo root: `python demo/demo_client.py`
5. Generated exports will appear in `backend/exports/`.

See the full README in the project for more details.
