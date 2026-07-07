# MINI GITOPS PROVISIONER
A lightweight GitOps platform that automates the build and deployment of containerized web applications to Kubernetes. The platform provides a simple deployment workflow while hiding the underlying Kubernetes complexity.

## Project Goals
- Understand modern GitOps workflows.
- Learn Kubernetes deployment automation.
- Build a lightweight internal developer platform.
- Explore CI/CD practices inspired by large engineering organizations.

## Architecture Overview
- GitHub Actions
- Docker
- AgroCD
- Helm
- Kubernetes

## Run locally
Documentation will be added as features are implemented.

## Future roadmap
### Phase 0

>Sample Application

### Phase 1

>Deployment pipeline
>
>Docker image
>GitHub Actions
>Helm
>Local Kubernetes

### Phase 2

>Provisioning API
>
>POST /deploy
>
>Automatic deployment requests.

### Phase 3

>Application management
>
>GET /applications
>GET /deployments
>DELETE /deployment/{id}

### Phase 4

>Git provider integration
>
>GitHub
>
>GitLab
>
>Automatic webhook handling.

### Phase 5

>Production features
>
>Authentication
>
>RBAC
>
>Logs
>
>Deployment history
>
>Rollbacks
>
>Multiple environments
