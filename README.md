# Universal Pattern Engine

[![CI](https://github.com/abidangit/universal-pattern-engine/actions/workflows/test.yml/badge.svg)](https://github.com/abidangit/universal-pattern-engine/actions)

A mathematical and computational engine for generating, transforming, analyzing, and discovering sequences and patterns.

Phase 1: the mathematical core — sequence abstractions, generators, analyzers, discovery heuristics, API, and an experiment harness.

Quick start:

- python -m venv .venv
- .\.venv\Scripts\activate
- pip install -r requirements.txt
- pytest
- Run API: `python cli.py run-api --host 0.0.0.0 --port 8000`

Local validation checklist:

- Install dependencies: `make install`
- Run linters and formatting: `make lint` and `pre-commit run --all-files`
- Run tests: `make test`
- Type-check (optional): `make typecheck`
- Build docs: `make docs`

Secrets and CI requirements:

See docs/ops/secrets.md for the list of GitHub repository secrets required to enable publishing, CI integrations, and runtime connections.

Releases and publishing:

- Tag a release: `git tag v0.1.0` then `git push --tags` to trigger release workflows that build images and publish to GHCR and PyPI (requires secrets configured).

Contributing:

See CONTRIBUTING.md for contribution guidelines and CODE_OF_CONDUCT.md for expected behavior.

