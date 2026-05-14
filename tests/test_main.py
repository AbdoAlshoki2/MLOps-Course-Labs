"""
Tests for the Churn Prediction API.

Run with:
    pytest tests/ -v
    pytest tests/ -v --cov=app --cov=main --cov-report=term-missing
"""

from litestar.testing import TestClient
from main import app
from schemas.prediction import PredictionRequest
from controllers.predictor import Predictor


predictor = Predictor()


# ---------------------------------------------------------------------------
# Function Tests
# ---------------------------------------------------------------------------
def test_predictor_function_directly():
    # Use mock data matching the BaseModel
    sample_data = PredictionRequest(
        CreditScore=600,
        Geography="France",
        Gender="Male",
        Age=40,
        Tenure=3,
        Balance=60000.0,
        NumOfProducts=2,
        HasCrCard=1,
        IsActiveMember=1,
        EstimatedSalary=50000.0,
    )
    result = predictor.predict(sample_data)

    assert hasattr(result, "ProbabilityOfExiting")
    assert 0.0 <= result.ProbabilityOfExiting <= 1.0


# ---------------------------------------------------------------------------
# Endpoint Tests
# ---------------------------------------------------------------------------
def test_get_root():
    with TestClient(app=app) as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Welcome to the Churn Prediction API!"}


def test_get_health():
    with TestClient(app=app) as client:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "healthy"}


def test_post_predict_valid():
    with TestClient(app=app) as client:
        payload = {
            "CreditScore": 600,
            "Geography": "France",
            "Gender": "Male",
            "Age": 40,
            "Tenure": 3,
            "Balance": 60000.0,
            "NumOfProducts": 2,
            "HasCrCard": 1,
            "IsActiveMember": 1,
            "EstimatedSalary": 50000.0,
        }

        response = client.post("/predict", json=payload)
        assert response.status_code == 201

        data = response.json()
        assert "ProbabilityOfExiting" in data
        assert 0.0 <= float(data["ProbabilityOfExiting"]) <= 1.0


def test_post_predict_invalid_input():
    with TestClient(app=app) as client:
        response = client.post("/predict", json={"Age": "Not a number"})

        assert response.status_code == 400
