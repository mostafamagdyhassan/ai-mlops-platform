
from contextlib import asynccontextmanager

from fastapi import FastAPI

from application.config import settings
from application.database import Base, engine
from application.models import Incident
from application.routes.health import router as health_router
from application.routes.incidents import router as incidents_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title=settings.app_name,
    description="API for an AI-powered IT Operations Platform.",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(health_router)
app.include_router(incidents_router)


@app.get("/", tags=["general"])
async def root() -> dict[str, str]:
    return {
        "name": settings.app_name,
        "status": "running",
        "docs": "/docs",
    }
