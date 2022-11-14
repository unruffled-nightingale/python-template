install:
	poetry install

update:
	poetry update

start:
	python main.py

test-all: test-integration test-unit

test-unit:
	pytest tests/unit -v --cov-config pyproject.toml --cov
	coverage xml --fail-under 90

test-integration:
	pytest tests/integration -v --cov-config pyproject.toml

check-all: check-poetry check-lint check-mypy check-bandit check-private-keys check-format

check-poetry:
	poetry check

check-lint:
	poetry run flake8 .

check-mypy:
	poetry run mypy --config-file pyproject.toml .

check-bandit:
	poetry run bandit -r -q . --exclude /tests

check-private-keys:
	poetry run detect-private-key

check-format:
	poetry run isort --check-only --diff .
	poetry run black --check --diff .

format:
	poetry run black .
	poetry run isort .
	poetry run end-of-file-fixer
	poetry run trailing-whitespace-fixer