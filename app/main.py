from fastapi import FastAPI
from app.core.config import settings
from app.api.routes.chat import router as chat_router
from app.api.routes.planner import router as planner_router


app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    description="Enterprise Multi-Agent AI Platform"
)



@app.get("/")
async def root():

    return {
        "message": "Welcome to NEXUS AI",
        "status": "running"
    }


@app.get("/health")
async def health():

    return {
        "status": "healthy",
        "application": settings.APP_NAME
    }

app.include_router(
    chat_router,
    prefix="/api/v1",
    tags=["AI Chat"]
)


app.include_router(
    planner_router,
    prefix="/api/v1",
    tags=["Agent Planner"]
)