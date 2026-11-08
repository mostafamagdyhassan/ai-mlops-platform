
import os
from pathlib import Path

from fastapi import APIRouter, HTTPException

from application.observability import ANOMALIES_DETECTED
from application.services.metrics_service import InfrastructureMetric

router = APIRouter(prefix="/anomaly", tags=["machine-learning"])

MODEL_PATH = os.getenv(
    "MODEL_PATH",
    "mlops/model-registry/anomaly_detector.joblib",
)

_detector = None


@router.get("/health")
def model_health():
    return {
        "model_available": Path(MODEL_PATH).exists(),
        "model_path": MODEL_PATH,
    }


@router.post("/predict")
def predict_anomaly(data: InfrastructureMetric):
    global _detector

    if not Path(MODEL_PATH).exists():
        raise HTTPException(
            status_code=503,
            detail="ML model is not trained or available.",
        )

    try:
        if _detector is None:
            from mlops.serving.predict import AnomalyDetector

            _detector = AnomalyDetector(MODEL_PATH)

        result = _detector.predict({
            "cpu_usage": data.cpu_usage,
            "memory_usage": data.memory_usage,
            "disk_usage": data.disk_usage,
            "network_traffic": data.network_traffic,
        })

        if result["is_anomaly"]:
            ANOMALIES_DETECTED.inc()

        return {
            "hostname": data.hostname,
            **result,
        }

    except ImportError as exc:
        raise HTTPException(
            status_code=503,
            detail="ML dependencies are not installed.",
        ) from exc
