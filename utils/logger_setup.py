"""
Logging configuration.
"""

import logging


def setup_logging():
    # Set up basic logging with level INFO
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    # Create a named logger using logging.getLogger() and return it
    logger = logging.getLogger("churn-prediction-api")
    return logger
