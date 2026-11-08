
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class IncidentCreate(BaseModel):
    title: str = Field(min_length=3, max_length=255)
    description: str = Field(min_length=5)
    severity: str = Field(default="medium", pattern="^(low|medium|high|critical)$")
    affected_service: str = Field(min_length=2, max_length=255)


class IncidentUpdate(BaseModel):
    status: str = Field(pattern="^(open|investigating|resolved)$")


class IncidentResponse(BaseModel):
    id: int
    title: str
    description: str
    severity: str
    affected_service: str
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
