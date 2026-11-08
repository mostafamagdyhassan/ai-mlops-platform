
# MLOps Pipeline

This module implements the infrastructure anomaly detection lifecycle.

## Pipeline

1. Generate infrastructure metrics.
2. Validate and preprocess datasets.
3. Split training and testing data.
4. Train an Isolation Forest model.
5. Evaluate model performance.
6. Track experiments with MLflow.
7. Save model artifacts.
8. Serve predictions through the API.

## Run the pipeline

Install dependencies:

```bash
pip install -e ".[ml]"
```

Run:

```bash
python mlops/pipelines/run_training.py
```

Start MLflow separately:

```bash
mlflow server --host 0.0.0.0 --port 5000
```

Open:

http://localhost:5000

## Model

Algorithm: Isolation Forest

Use case: Infrastructure anomaly detection.

Features:
- CPU utilization
- Memory utilization
- Disk utilization
- Network traffic

Note: The initial dataset is synthetic. Model performance on synthetic data does not establish production accuracy. Real infrastructure data and proper validation are required before operational use.
