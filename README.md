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

## 🚀 Progress & Implementation Steps

### Step 1: Backend Foundation
* **FastAPI Application Setup**: Web backend running on `app/main.py`.
* **Health Check Endpoint**: `GET /health` returning service status.
* **Environment Configuration**: Decoupled config management via `pydantic-settings`.
* **Logging & Testing**: Standard stdout logging and initial `pytest` test suite.

### Step 2: Simulated Payment Service (Production System Simulation)
* **Pydantic Schemas** (`app/schemas/payment.py`): Validation for `CreatePaymentRequest` and response formatting for `PaymentResponse`.
* **Domain Model** (`app/models/payment.py`): `PaymentModel` dataclass representing stored payment records.
* **Repository Layer** (`app/repositories/payment_repository.py`): In-memory storage abstraction with `create`, `get_by_id`, and `get_all` operations.
* **Service Layer** (`app/services/payment_service.py`): Core payment processing logic, deterministic status resolution, latency tracking (`processing_time_ms`), and structured logging.
* **API Layer** (`app/api/v1/payments.py`): RESTful endpoints (`POST /payments`, `GET /payments/{payment_id}`, `GET /payments`).
* **Automated Tests** (`tests/test_payments.py`): Tests covering creation, retrieval, listing, 404 handling, and validation errors (422).

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
* **Create Payment**: `POST http://127.0.0.1:8000/payments`
* **List Payments**: `GET http://127.0.0.1:8000/payments`
* **Interactive API Docs (Swagger UI)**: `http://127.0.0.1:8000/docs`

### 5. Run Automated Tests
Execute the test suite using `pytest`:

```bash
python -m pytest
```
