# Quality Guardian

**Enterprise Release Quality Guardian — Multi-Agent QA Automation**

Quality Guardian is an AI-powered multi-agent framework (FastAPI backend + React dashboard) that automates requirement analysis, test-case generation, coverage checks and release-quality scoring for enterprise software projects. This repository contains a runnable prototype, clear architecture, and instructions to extend it into a production-ready system.

---

## Table of Contents

* [Project Overview](#project-overview)
* [Features (Prototype)](#features-prototype)
* [Architecture](#architecture)
* [Tech Stack](#tech-stack)
* [Repository Layout](#repository-layout)
* [Prerequisites](#prerequisites)
* [Quick Start (Local)](#quick-start-local)
* [Run Demo Client](#run-demo-client)
* [Development Notes](#development-notes)
* [How to Extend / Next Steps](#how-to-extend--next-steps)
* [Testing & Evaluation](#testing--evaluation)
* [License](#license)
* [Contact / Author](#contact--author)

---

## Project Overview

Quality Guardian demonstrates a practical multi-agent approach to automating software test documentation and release-quality decisions. The prototype focuses on:

* Parsing requirement text into testable features
* Generating structured test cases
* Exporting artifacts (CSV / PDF)
* Maintaining a small memory bank of reviewer edits
* Providing a simple API and demo client

This version is intentionally lightweight so you can run it locally and extend parts (LLM, vector DB, observability) later.

---

## Features (Prototype)

* Requirement ingestion (POST /requirements)
* Simple rule-based NLP analyzer for feature extraction
* Template-driven test case generator (replaceable by LLM)
* In-memory job store and memory bank
* CSV and PDF export of generated test cases
* Demo client to submit sample requirements and see outputs

---

## Architecture

The system is modular and built around an **Orchestrator** that coordinates small "agent" modules:

* **Requirements Analyzer Agent** (nlp.py) — extracts features from text
* **Test Case Generator Agent** (generator.py) — builds test cases from features
* **Memory Agent** (memory.py) — stores reviewer edits & patterns
* **Export Tool** (exporter.py) — creates CSV/PDF artifacts
* **Orchestrator** (orchestrator.py) — coordinates the flow

The prototype uses a FastAPI backend. In a production system, agents would be microservices communicating via A2A messages and a job queue.

---

## Tech Stack

* Backend: **Python 3.10+**, **FastAPI**, **Uvicorn**
* Frontend (recommended): **React.js** (not included in prototype)
* Database: **MongoDB** (prototype uses in-memory / JSON file)
* Exports: **ReportLab** for PDFs
* NLP: simple rule-based parsing (nltk is included for future expansion)

---

## Repository Layout

```
quality-guardian/
├── README.md
├── requirements.txt
├── backend/
│   ├── app.py                # FastAPI server
│   ├── models.py             # Pydantic models
│   ├── nlp.py                # Requirement analyzer (agent)
│   ├── generator.py          # Test case generator (agent)
│   ├── memory.py             # Simple memory bank
│   ├── orchestrator.py       # Agent orchestrator
│   ├── exporter.py           # CSV / PDF export tool
│   ├── jobs.py               # In-memory job store
│   └── sample_data/
│       └── sample_requirements.json
├── demo/
│   └── demo_client.py        # Simple demo client
└── docs/
    └── architecture.md
```

---

## Prerequisites

* Python 3.10 or newer
* pip
* (Optional) Docker & docker-compose if you prefer containerized run

Install Python dependencies:

```bash
python -m venv .venv
# activate virtualenv (Mac/Linux)
source .venv/bin/activate
# Windows PowerShell
# .\\.venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
```

**Note:** If you use `nltk`, you may need to run a first-time download of models in a Python shell:

```python
import nltk
nltk.download('punkt')
```

---

## Quick Start (Local)

1. Start the FastAPI backend from the `backend/` directory:

```bash
cd backend
uvicorn app:app --reload --port 8000
```

2. In another terminal, run the demo client from repo root:

```bash
python demo/demo_client.py
```

3. Watch console logs for job status and generated testcases. Exports are placed in `backend/exports/`.

---

## Run Demo Client

`demo/demo_client.py` submits a sample requirement and polls for job status. It prints the generated test cases and requests an export (CSV by default). Review the files in `backend/exports/` to see the produced artifacts.

---

## Development Notes

* Replace the rule-based generator with an LLM-backed `generator_llm.py` for improved quality. Use a tool interface for LLM calls to avoid embedding keys.
* Swap the in-memory job store for MongoDB and add a worker queue (Redis/RQ or RabbitMQ) to scale parallel agents.
* Add an InMemorySessionService and Memory Bank backed by a vector DB (FAISS / Milvus) for long-term memory and similarity search.
* Instrument the system with OpenTelemetry, Prometheus, and Grafana for observability.

---

## How to Extend / Next Steps

1. **LLM Integration**: Create an LLM client wrapper and an agent that composes context + prompt templating.
2. **Agent Engine**: Convert modules to microservices with A2A JSON messaging and job queue workers.
3. **Frontend Dashboard**: Build a React app for review, editing, and export management.
4. **Evaluation Suite**: Add gold dataset and evaluation scripts to compute precision/recall and acceptance rates.
5. **Deployment**: Dockerize services and create `docker-compose.yml` for local production-like testing.

---

## Testing & Evaluation

* Add unit tests for `nlp.extract_features()` and `generator.generate_testcases()`.
* Create a gold dataset of ~20 requirements and expected test cases to compute precision/recall.
* Add a simple metrics collector to log counts of generated testcases and acceptance rates.

---


