## Purpose
This application is intentionally simple.

It serves as a deployment target for the Mini GitOps Provisioner platform and demonstrates automated deployments through CI/CD and Kubernetes.

## How to run:
APP_VERSION=1.0.0 COMMIT_SHA=abc123 ENVIRONMENT=dev uv run uvicorn app.main:app --reload
