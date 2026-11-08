
from pathlib import Path

import joblib
import pandas as pd

FEATURES = [
    "cpu_usage",
    "memory_usage",
    "disk_usage",
    "network_traffic",
]


class AnomalyDetector:

    def __init__(self, model_path: str):
        path = Path(model_path)

        if not path.exists():
            raise FileNotFoundError(
                f"Model not found: {model_path}"
            )

        self.model = joblib.load(path)

    def predict(self, metrics: dict) -> dict:
        data = pd.DataFrame(
            [metrics],
            columns=FEATURES,
        )

        prediction = int(
            self.model.predict(data)[0] == -1
        )

        score = float(
            self.model.decision_function(data)[0]
        )

        return {
            "is_anomaly": bool(prediction),
            "prediction": "anomaly" if prediction else "normal",
            "anomaly_score": score,
        }
