"""
Model loading and prediction logic.

The model must be loaded ONCE at module level, NOT inside the predict function.
"""

import pickle
import joblib
import pandas as pd
from pathlib import Path
from schemas.prediction import PredictionRequest, PredictionResponse

# TODO 1: Load your serialized churn model from data/model.joblib


class Predictor:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Predictor, cls).__new__(cls)

            base_dir = Path(__file__).resolve().parent.parent

            with open(base_dir / "models" / "model.pkl", "rb") as f:
                cls._instance.model = pickle.load(f)

            cls._instance.preprocessor = joblib.load(
                base_dir / "models" / "column_transformer.joblib"
            )

        return cls._instance

    def _preprocess(self, X: PredictionRequest):
        df = pd.DataFrame(
            {
                "CreditScore": [X.CreditScore],
                "Geography": [X.Geography],
                "Gender": [X.Gender],
                "Age": [X.Age],
                "Tenure": [X.Tenure],
                "Balance": [X.Balance],
                "NumOfProducts": [X.NumOfProducts],
                "HasCrCard": [X.HasCrCard],
                "IsActiveMember": [X.IsActiveMember],
                "EstimatedSalary": [X.EstimatedSalary],
            }
        )
        return self.preprocessor.transform(df)

    def predict(self, X: PredictionRequest) -> PredictionResponse:
        X_preprocessed = self._preprocess(X)
        return PredictionResponse(
            probability=self.model.predict_proba(X_preprocessed)[:, 1][0]
        )
