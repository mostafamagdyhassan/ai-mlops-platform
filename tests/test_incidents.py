
from fastapi.testclient import TestClient

from application.main import app

client = TestClient(app)


def test_create_incident():
    response = client.post(
        "/incidents/",
        json={
            "title": "High CPU utilization",
            "description": "CPU utilization exceeded 90 percent.",
            "severity": "high",
            "affected_service": "web-server",
        },
    )

    assert response.status_code == 201

    result = response.json()

    assert result["title"] == "High CPU utilization"
    assert result["severity"] == "high"
    assert result["status"] == "open"


def test_invalid_incident_severity():
    response = client.post(
        "/incidents/",
        json={
            "title": "Test incident",
            "description": "Testing invalid severity.",
            "severity": "unknown",
            "affected_service": "api",
        },
    )

    assert response.status_code == 422
