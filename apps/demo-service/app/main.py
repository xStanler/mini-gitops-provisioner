from fastapi import FastAPI
import os
import socket

APP_VERSION = os.getenv("APP_VERSION", "local")
COMMIT_SHA = os.getenv("COMMIT_SHA", "local")
ENVIRONMENT = os.getenv("ENVIRONMENT", "local")
HOSTNAME = socket.gethostname()

app = FastAPI()

@app.get("/")
async def get_root() -> dict:
    return {
        "name": "demo-service",
        "version": APP_VERSION,
        "commit_sha": COMMIT_SHA,
        "environment": ENVIRONMENT,
        "hostname": HOSTNAME
        }

@app.get("/health")
async def check_health() -> dict:
    return {
            "status": "ok"
            }

@app.get("/ready")
async def get_ready() -> dict:
    return {"status": "ready"}
