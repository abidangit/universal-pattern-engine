# Developer Guide

Local setup
1. python -m venv .venv
2. .\.venv\Scripts\activate
3. make install
4. pre-commit install

Run API
- python cli.py run-api --host 0.0.0.0 --port 8000
- Open http://localhost:8000/docs for OpenAPI UI

Run tests
- make test
- pytest -q

Run Celery worker (local)
- Start Redis (docker run -p 6379:6379 redis)
- celery -A pattern_engine.tasks.celery_app worker --loglevel=info

Database migrations
- Configure DATABASE_URL or use sqlite (default)
- alembic upgrade head

Debugging tips
- Use logging_config.setup_logging('DEBUG') in scripts
- Use pytest -k <name> to run focused tests

Developer workflow summary
- Branch → Code → Tests → Pre-commit → PR → CI → Merge
