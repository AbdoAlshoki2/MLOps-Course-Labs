from pydantic import BaseModel


class PredictionRequest(BaseModel):
    CreditScore: int
    Geography: str
    Gender: str
    Age: int
    Tenure: int
    Balance: float
    NumOfProducts: int
    HasCrCard: int
    IsActiveMember: int
    EstimatedSalary: float


class PredictionResponse(BaseModel):
    ProbabilityOfExiting: float
