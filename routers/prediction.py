from litestar import post, Controller
from schemas.prediction import PredictionRequest, PredictionResponse
from controllers.predictor import Predictor
from utils.logger_setup import setup_logging

logger = setup_logging()
predictor = Predictor()


class PredictionController(Controller):
    path = "/predict"

    @post()
    async def create_prediction(self, data: PredictionRequest) -> PredictionResponse:
        logger.info(
            f"Received prediction request for user with CreditScore {data.CreditScore}"
        )

        try:
            result = predictor.predict(data)
            logger.info(
                f"Prediction successful. Probability of exiting: {result.ProbabilityOfExiting:.4f}"
            )
            return result
        except Exception as e:
            logger.error(f"Error during prediction: {e}")
            raise
