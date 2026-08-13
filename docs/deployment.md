# Deployment Guide

This guide describes deploying UPE in common environments.

Prerequisites
- Docker & docker-compose
- Kubernetes cluster & helm
- GitHub Actions secrets: DATABASE_URL, REDIS_URL, PYPI_API_TOKEN, GHCR_PAT

Docker Compose (local)
1. Copy .env.example → .env and set DATABASE_URL (sqlite or postgres) and REDIS_URL.
2. docker compose up --build
3. API available at http://localhost:8000
4. Run migrations: make migrate (uses DATABASE_URL)

Kubernetes (production, using Helm)
1. Build & push image to GHCR: tag and push or use GH Actions release workflow.
2. helm upgrade --install upe k8s/helm/universal-pattern-engine -n upe --create-namespace \
     --set image.repository=ghcr.io/OWNER/universal-pattern-engine,image.tag=latest
3. Provide secrets via kubernetes secret (DATABASE_URL, REDIS_URL)
4. Run Alembic migrations against the production DB

Workers
- Run Celery workers: celery -A pattern_engine.tasks.celery_app worker --loglevel=info
- Use Redis as the broker/back-end (REDIS_URL)

Observability
- Expose Prometheus metrics via prometheus-client where appropriate
- Add Grafana dashboards for experiment metrics and queue lengths

Backup & migrations
- Use alembic for schema migrations (alembic upgrade head)
- Backup Postgres with pg_dump and store artifacts securely

Security
- Use GitHub secrets for tokens
- Do not commit credentials
- Run security scans (bandit, trivy) in CI

Scaling
- Horizontal scale API pods behind a load balancer
- Separate worker pool types (polynomial-search, stochastic, chaos)
- Use a queue system (Redis/RabbitMQ) and autoscale workers based on queue length
