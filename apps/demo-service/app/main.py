from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os

APP_VERSION = os.getenv("APP_VERSION", "local")
COMMIT_SHA = os.getenv("COMMIT_SHA", "local")
ENVIRONMENT = os.getenv("ENVIRONMENT", "local")

app = FastAPI()

@app.get("/")
async def get_root():
    return JSONResponse(content={
        "name": "demo-service",
        "version": APP_VERSION,
        "commit_sha": COMMIT_SHA,
        "environment": ENVIRONMENT,
        "hostname": "..."
        }, status_code=200)

@app.get("/health")
async def check_health():
    return """ {"status": "ok"} """

@app.get("/ready")
async def get_ready():
    return """ {"status": "ready"} """
