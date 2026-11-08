
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter(prefix="/ai", tags=["artificial-intelligence"])


class IncidentAnalysisRequest(BaseModel):
    incident: str = Field(min_length=5, max_length=10000)


@router.post("/analyze")
async def analyze_incident(data: IncidentAnalysisRequest):
    try:
        from ai.agents.incident_agent import IncidentAssistant

        assistant = IncidentAssistant()

        return await assistant.analyze(data.incident)

    except ImportError as exc:
        raise HTTPException(
            status_code=503,
            detail="AI dependencies are not installed.",
        ) from exc

    except Exception as exc:
        raise HTTPException(
            status_code=503,
            detail="AI assistant is unavailable. Check Ollama and Qdrant.",
        ) from exc
