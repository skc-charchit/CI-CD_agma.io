"""Shared platform API entry point."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.courses import router as courses_router


app = FastAPI(
    title="AGMA.io Platform API",
    description="Shared APIs for the AGMA.io company website and products.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

app.include_router(courses_router, prefix="/api/v1")
