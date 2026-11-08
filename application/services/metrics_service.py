
from datetime import datetime, timezone

from pydantic import BaseModel, Field


class InfrastructureMetric(BaseModel):
    hostname: str
    cpu_usage: float = Field(ge=0, le=100)
    memory_usage: float = Field(ge=0, le=100)
    disk_usage: float = Field(ge=0, le=100)
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )


# Temporary in-memory storage for the first development milestone.
# We will move metric persistence to PostgreSQL in the next iteration.
_metrics: list[InfrastructureMetric] = []


def ingest_metric(metric: InfrastructureMetric) -> InfrastructureMetric:
    _metrics.append(metric)
    return metric


def get_metrics() -> list[InfrastructureMetric]:
    return _metrics[-1000:]


def clear_metrics() -> None:
    _metrics.clear()
