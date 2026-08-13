.PHONY: install test docker-build

install:
	python -m pip install --upgrade pip && pip install -r requirements.txt

test:
	pytest -q

docker-build:
	docker build -t universal-pattern-engine:local .
