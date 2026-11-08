
from sqlalchemy import select
from sqlalchemy.orm import Session

from application.models.incident import Incident
from application.schemas.incident import IncidentCreate


def create_incident(db: Session, data: IncidentCreate) -> Incident:
    incident = Incident(**data.model_dump())

    db.add(incident)
    db.commit()
    db.refresh(incident)

    return incident


def get_incidents(db: Session) -> list[Incident]:
    statement = select(Incident).order_by(Incident.created_at.desc())
    return list(db.scalars(statement).all())


def get_incident(db: Session, incident_id: int) -> Incident | None:
    return db.get(Incident, incident_id)


def update_incident_status(
    db: Session,
    incident: Incident,
    status: str,
) -> Incident:
    incident.status = status

    db.commit()
    db.refresh(incident)

    return incident
