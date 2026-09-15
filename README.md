# OpsPilot

OpsPilot is an AI-powered incident investigation platform designed to help developers and operations teams understand production issues faster.

It simulates a payment service and investigates incidents such as slow requests, database problems, service failures, and other operational issues. The goal is to collect system evidence, identify possible root causes, and provide a clear explanation of what happened and what should be checked next.

## What It Does

* Monitors a simulated payment service
* Collects application and system signals such as logs, metrics, and errors
* Investigates incidents using multiple sources of evidence
* Uses operational documentation and runbooks as supporting context
* Provides root-cause analysis and recommended actions
* Keeps investigation state so multiple checks can be combined into one workflow

## Architecture

```text
React Dashboard
      |
    FastAPI
      |
  LangGraph
   /     \
 RAG     MCP
 |        |
Runbooks  System Tools
          |
   Logs / Metrics / DB
```

## Tech Stack

* Python
* FastAPI
* PostgreSQL
* Redis
* LangGraph
* RAG
* MCP
* LLM APIs
* React
* Docker

## Example

A payment service starts responding slowly.

OpsPilot can investigate the incident by checking:

1. Service latency and error metrics
2. Recent application logs
3. Database performance
4. Relevant troubleshooting documentation
5. Recent system changes

It then combines the evidence to identify the most likely cause and explain the reasoning behind the result.

## Running Locally

Clone the repository and install the backend dependencies:

```bash
cd backend
pip install -r requirements.txt
```

Start the API:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

## Project Status

OpsPilot is being developed as a production-style engineering project focused on AI-assisted incident investigation, tool-based system access, retrieval-augmented reasoning, and stateful agent workflows.
