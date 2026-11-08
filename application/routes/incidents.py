
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from application.database import get_db
from application.schemas.incident import (
    IncidentCreate,
    IncidentResponse,
    IncidentUpdate,
)
from application.services import incident_service

router = APIRouter(prefix="/incidents", tags=["incidents"])


@router.post(
    "/",
    response_model=IncidentResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_incident(
    data: IncidentCreate,
    db: Session = Depends(get_db),
):
    return incident_service.create_incident(db, data)


@router.get("/", response_model=list[IncidentResponse])
def list_incidents(db: Session = Depends(get_db)):
    return incident_service.get_incidents(db)


@router.get("/{incident_id}", response_model=IncidentResponse)
def get_incident(
    incident_id: int,
    db: Session = Depends(get_db),
):
    incident = incident_service.get_incident(db, incident_id)

    if incident is None:
        raise HTTPException(
            status_code=404,
            detail="Incident not found",
        )

    return incident


@router.patch("/{incident_id}", response_model=IncidentResponse)
def update_incident(
    incident_id: int,
    data: IncidentUpdate,
    db: Session = Depends(get_db),
):
    incident = incident_service.get_incident(db, incident_id)

    if incident is None:
        raise HTTPException(
            status_code=404,
            detail="Incident not found",
        )

    return incident_service.update_incident_status(
        db,
        incident,
        data.status,
    )
