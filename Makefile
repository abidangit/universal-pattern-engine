.PHONY: install test docker-build lint typecheck docs build publish-pypi migrate

install:
	python -m pip install --upgrade pip && pip install -r requirements.txt && pip install -e .

test:
	pytest -q

lint:
	pre-commit run --all-files

typecheck:
	mypy src || true

docs:
	mkdocs build

build:
	python -m build

publish-pypi:
	python -m pip install --upgrade twine
	python -m twine upload dist/*

migrate:
	alembic upgrade head

docker-build:
	docker build -t universal-pattern-engine:local .
