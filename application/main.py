
from fastapi import FastAPI

from application.config import settings
from application.routes.health import router as health_router

app = FastAPI(
    title=settings.app_name,
    description="API for an AI-powered IT Operations Platform.",
    version="0.1.0",
)

app.include_router(health_router)


@app.get("/", tags=["general"])
async def root() -> dict[str, str]:
    return {
        "name": settings.app_name,
        "status": "running",
        "docs": "/docs",
    }
