"""
Simple runner that reads config.yaml and runs multiple experiments.
"""

import yaml
import os
import mlflow
from train import main
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
import logging

import warnings
warnings.filterwarnings("ignore")

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(handler)


def run_experiments(config_path=None):
    """
    Run all experiments defined in the config file.
    """
    if config_path is None:
        config_path = os.path.join(os.path.dirname(__file__), "config.yaml")
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    mlflow.set_tracking_uri("mlruns")

    logger.info(f"Running {len(config['runs'])} experiments...")

    model_map = {
        "LogisticRegression": LogisticRegression,
        "SVC": SVC,
        "RandomForestClassifier": RandomForestClassifier
    }
    for run_config in config['runs']:
        run_name = run_config['name']
        model_type = run_config['model_type']
        params = run_config['params']
        model_class = model_map[model_type]
        logger.info(f"Starting experiment: {run_name} with model {model_type}")
        main(run_name=run_name, model_class=model_class, params=params)
        logger.info(f"Finished experiment: {run_name}")
        


if __name__ == "__main__":
    run_experiments()