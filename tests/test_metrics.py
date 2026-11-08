
from fastapi.testclient import TestClient

from application.main import app
from application.services.metrics_service import clear_metrics

client = TestClient(app)


def test_ingest_infrastructure_metric():
    clear_metrics()

    response = client.post(
        "/metrics/ingest",
        json={
            "hostname": "server-01",
            "cpu_usage": 75.5,
            "memory_usage": 60.0,
            "disk_usage": 45.0,
        },
    )

    assert response.status_code == 200
    assert response.json()["hostname"] == "server-01"


def test_reject_invalid_metric():
    response = client.post(
        "/metrics/ingest",
        json={
            "hostname": "server-01",
            "cpu_usage": 150,
            "memory_usage": 60,
            "disk_usage": 45,
        },
    )

    assert response.status_code == 422
