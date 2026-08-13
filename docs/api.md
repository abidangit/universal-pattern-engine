# API Reference

The API is implemented with FastAPI and exposes the following endpoints (also available at /docs when running locally):

POST /analyze
- Payload: {"sequence": [number, ...]}
- Returns: classification and analysis data (classification, confidence, details)

POST /discover
- Payload: {"sequence": [number, ...]}
- Returns: discovered candidate explanation (classification, formula, confidence)

POST /generate
- Payload: {"type": "arithmetic|geometric|fibonacci", "params": { ... }}
- Returns: {"sequence": [...]} generated sequence

POST /experiments/run
- Payload: {"name": "exp1", "type": "arithmetic", "params": {"start":0, "diff":1, "n":100}}
- Runs experiment, persists result, returns result and db_id

GET /experiments
- Returns: recent experiments (id, name, status, created_at)

OpenAPI
- FastAPI provides OpenAPI schema at /openapi.json and interactive docs at /docs (SwaggerUI) and /redoc
