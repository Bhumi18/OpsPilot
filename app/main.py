import logging
from fastapi import FastAPI
from app.core.config import settings
from app.core.logging import setup_logging

# Configure logging at application startup
setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.APP_NAME,
    description="OpsPilot API - AI Incident Investigation & Root Cause Analysis Platform",
    version="0.1.0"
)

logger.info(f"Starting {settings.APP_NAME} in [{settings.ENVIRONMENT}] environment")


@app.get("/health")
def health_check():
    """Health check endpoint to verify backend service operational status."""
    return {
        "status": "ok",
        "service": "opspilot-api"
    }
