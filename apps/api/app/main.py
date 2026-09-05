"""Shared platform API entry point."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.courses import router as courses_router
from app.config import get_settings


settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    description="Shared APIs for the AGMA.io company website and products.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_methods=["GET"],
    allow_headers=["*"],
)

app.include_router(courses_router, prefix="/api/v1")
