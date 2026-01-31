# Bank Customer Churn Prediction

## Overview

This project helps you test different machine learning models to predict if a bank customer will leave (churn) or stay. You can easily try different models and settings, and see the results using MLflow.

Supported models include:
- Logistic Regression
- Support Vector Machine (SVC)
- Random Forest

## Setup

Clone the repository and navigate to the project root directory:

```shell
cd MLOps-Course-Labs
```

To run this application, you need Python 3.12. You can download it from the [official Python website](https://www.python.org/downloads/release/python-3120/).

Create a virtual environment using Python 3.12:

On Windows:
```shell
python -m venv .venv
.venv\Scripts\activate
```

On macOS/Linux:
```shell
python3 -m venv .venv
source .venv/bin/activate
```

Alternatively, you can use [uv](https://github.com/astral-sh/uv):

```shell
uv venv .venv
uv venv .venv --python 3.12
```

## Installation

From the root of the project, install the required dependencies:

```shell
pip install -r requirements.txt
```

## Running Experiments

To run all experiments defined in the configuration file:

```shell
python src/runner.py
```

## Viewing Results

To view experiment results and artifacts, start the MLflow UI in a new terminal:

```shell
mlflow ui
```

Then open your browser and go to [http://localhost:5000](http://localhost:5000) to explore the experiment runs and metrics.



## Notes
You will see two created folders when you run the script `python src\runner.py`, the `artifacts` and `mlruns`
- `artifacts`: this folder contains the confussion matrix for each model.
- `mlruns`: this folder contains the run files that is used by MLflow.