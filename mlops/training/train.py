
import argparse
import json
from pathlib import Path

import joblib
import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import (
    classification_report,
    f1_score,
    precision_score,
    recall_score,
)

FEATURES = [
    "cpu_usage",
    "memory_usage",
    "disk_usage",
    "network_traffic",
]


def train_model(
    train_path: str,
    test_path: str,
    output_dir: str,
    tracking_uri: str,
):
    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)

    X_train = train[FEATURES]
    X_test = test[FEATURES]
    y_test = test["is_anomaly"]

    model = IsolationForest(
        n_estimators=200,
        contamination=0.05,
        random_state=42,
    )

    normal_training_data = train[
        train["is_anomaly"] == 0
    ][FEATURES]

    model.fit(normal_training_data)

    predictions = (model.predict(X_test) == -1).astype(int)

    precision = precision_score(
        y_test,
        predictions,
        zero_division=0,
    )
    recall = recall_score(
        y_test,
        predictions,
        zero_division=0,
    )
    f1 = f1_score(
        y_test,
        predictions,
        zero_division=0,
    )

    mlflow.set_tracking_uri(tracking_uri)
    mlflow.set_experiment("infrastructure-anomaly-detection")

    with mlflow.start_run():
        mlflow.log_params({
            "algorithm": "IsolationForest",
            "n_estimators": 200,
            "contamination": 0.05,
            "features": FEATURES,
        })

        mlflow.log_metrics({
            "precision": precision,
            "recall": recall,
            "f1_score": f1,
        })

        mlflow.sklearn.log_model(
            model,
            name="anomaly_detector",
        )

        output = Path(output_dir)
        output.mkdir(parents=True, exist_ok=True)

        model_path = output / "anomaly_detector.joblib"
        joblib.dump(model, model_path)

        report = classification_report(
            y_test,
            predictions,
            output_dict=True,
            zero_division=0,
        )

        (output / "evaluation.json").write_text(
            json.dumps(report, indent=2),
            encoding="utf-8",
        )

    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1 Score: {f1:.4f}")
    print(f"Model saved to {model_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--train",
        default="mlops/data/processed/train.csv",
    )
    parser.add_argument(
        "--test",
        default="mlops/data/processed/test.csv",
    )
    parser.add_argument(
        "--output",
        default="mlops/model-registry",
    )
    parser.add_argument(
        "--tracking-uri",
        default="http://localhost:5000",
    )

    args = parser.parse_args()

    train_model(
        args.train,
        args.test,
        args.output,
        args.tracking_uri,
    )
