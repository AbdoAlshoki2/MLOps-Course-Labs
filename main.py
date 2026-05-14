"""
Churn Prediction API

Run with:
    litestar --app main:app run --reload
Then open:
    http://localhost:8000/schema/swagger
"""

from litestar import Litestar, get

from utils.logger_setup import setup_logging
from routers.prediction import PredictionController

logger = setup_logging()


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------


@get("/")
async def index() -> dict:
    logger.info("Home endpoint accessed.")
    return {"message": "Welcome to the Churn Prediction API!"}


@get("/health")
async def health() -> dict:
    return {"status": "healthy"}


# ---------------------------------------------------------------------------
# App
# ---------------------------------------------------------------------------

app = Litestar(
    route_handlers=[
        index,
        health,
        PredictionController,
    ],
)
