# OpsPilot — AI Incident Investigation & Root Cause Analysis Platform

## 📌 Project Overview
**OpsPilot** is an intelligent site reliability engineering (SRE) platform designed to assist DevOps and SRE teams during active production incidents. By connecting AI-driven analysis with system telemetry, logs, and architectural documentation, OpsPilot accelerates Root Cause Analysis (RCA) and provides actionable remediation guidance.

## 🎯 Overall Goal of the Project
The ultimate objective of OpsPilot is to automate complex, time-consuming incident investigation workflows:
* **Telemetry & Log Retrieval**: Ingest and index real-time system logs and metrics.
* **Knowledge Contextualization**: Retrieve technical documentation and architecture diagrams using Retrieval-Augmented Generation (RAG).
* **Automated Investigation**: Employ autonomous AI Agents (built with LangGraph and MCP) to analyze metric anomalies, perform root cause deduction, and draft incident reports.
* **Interactive Dashboard**: Provide an intuitive web workspace for engineers to interact with AI co-pilots during high-pressure incident response calls.

---

## 🚀 Step 1 Implementation Summary
In this initial step, we established the foundational FastAPI backend architecture:
* **FastAPI Application Setup**: Minimal web backend running on `app/main.py`.
* **Health Check Endpoint**: `GET /health` returning service status.
* **Environment Configuration**: Decoupled config management via `pydantic-settings`.
* **Basic Logging**: Configurable log streaming to standard output.
* **Automated Testing**: Unit test suite using `pytest` and FastAPI `TestClient`.
* **Folder Architecture**: Modular layout (`api/`, `core/`, `models/`, `schemas/`, `services/`) ready for incremental capability additions in upcoming steps.

---

## 🛠️ Getting Started

### 1. Create a Virtual Environment
Navigate to the `backend` directory and create a Python virtual environment:

```bash
cd backend
python -m venv .venv
```

Activate the virtual environment:
* **Windows (PowerShell)**:
  ```powershell
  .venv\Scripts\Activate.ps1
  ```
* **macOS / Linux**:
  ```bash
  source .venv/bin/activate
  ```

### 2. Environment Variables Configuration
Copy the `.env.example` file to `.env`:

```bash
cp .env.example .env
```

### 3. Install Dependencies
Install all required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Start FastAPI Server
Run the FastAPI application locally using `uvicorn`:

```bash
uvicorn app.main:app --reload --port 8000
```

Once running, access:
* **Health Check**: `http://127.0.0.1:8000/health`
* **Interactive API Docs (Swagger UI)**: `http://127.0.0.1:8000/docs`
* **Alternative API Docs (ReDoc)**: `http://127.0.0.1:8000/redoc`

### 5. Run Automated Tests
Execute the test suite using `pytest`:

```bash
PYTHONPATH=. pytest
```
