# Required GitHub Secrets and Service Credentials

To enable CI, publishing, and runtime integrations, set the following repository secrets in GitHub (Settings → Secrets → Actions):

- PYPI_API_TOKEN: API token for publishing to PyPI (used by publish-pypi.yml)
- GHCR_PAT or GITHUB_TOKEN: used by release workflows to push container images to GitHub Container Registry (GHCR)
- CODECOV_TOKEN: optional, for Codecov uploads
- DOCKERHUB_TOKEN / DOCKERHUB_USERNAME: if publishing to Docker Hub
- DATABASE_URL: connection string for production database (used by Alembic migrations and app)
- REDIS_URL: Redis URL for Celery broker/back-end

Security: restrict secrets to org owners where appropriate and rotate tokens periodically.
