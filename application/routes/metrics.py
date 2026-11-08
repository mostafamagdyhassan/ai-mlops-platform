
from fastapi import APIRouter

from application.services.metrics_service import (
    InfrastructureMetric,
    get_metrics,
    ingest_metric,
)

router = APIRouter(prefix="/metrics", tags=["metrics"])


@router.post("/ingest", response_model=InfrastructureMetric)
def ingest(data: InfrastructureMetric):
    return ingest_metric(data)


@router.get("/", response_model=list[InfrastructureMetric])
def list_metrics():
    return get_metrics()
