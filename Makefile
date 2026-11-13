# LANTERN developer commands
#
#   make setup   ->  venv + dev deps + pre-commit hooks
#   make check   ->  what CI runs (lint + tests + status)
#   make status  ->  the lantern banner and campaign progress

PY ?= python3
VENV := .venv
BIN := $(VENV)/bin

.PHONY: setup check lint test status mappack clean

setup:
	$(PY) -m venv $(VENV)
	$(BIN)/pip install -e ".[dev]" pre-commit
	$(BIN)/pre-commit install

lint:
	$(BIN)/ruff check .

test:
	$(BIN)/pytest -q

status:
	$(BIN)/python scripts/lantern_status.py

check: lint test status

mappack:
	bash mappack/build.sh

clean:
	rm -rf $(VENV) .pytest_cache .ruff_cache *.egg-info
	find . -name __pycache__ -type d -prune -exec rm -rf {} +
