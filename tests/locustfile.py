from locust import HttpUser, task, between


class ChurnPredictionUser(HttpUser):
    # Wait between 1 and 3 seconds between tasks
    wait_time = between(1, 3)

    @task(1)
    def check_health(self):
        """Test the health check endpoint"""
        self.client.get("/health")

    @task(1)
    def check_home(self):
        """Test the home endpoint"""
        self.client.get("/")

    @task(5)
    def make_prediction(self):
        """Test the main model prediction endpoint"""
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
        # Assuming the API expects JSON
        self.client.post("/predict", json=payload)
