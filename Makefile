install:
	poetry install

update:
	poetry update

schedule-mac:
	sh ./scripts/schedule-mac.sh

run-mac:
	sh ./scripts/run-mac.sh

build-french-data:
	python -c "from language_wallpaper.main import build_language_data; build_language_data('french')"

run-french-wallpaper:
	python -c "from  language_wallpaper.main import run; run('french')"

test-unit:
	pytest tests/unit -v --cov-config pyproject.toml --cov
	coverage xml --fail-under 90

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