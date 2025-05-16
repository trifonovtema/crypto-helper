# Makefile for Crypto Helper project

PYTHON = python
UV = uv
VENV_DIR = .venv
ACTIVATE = source $(VENV_DIR)/bin/activate

.PHONY: help install run lint pre-commit format clean

help:
	@echo "Available commands:"
	@echo "  make install     - Create virtualenv and install dependencies using uv"
	@echo "  make lint        - Run linters"
	@echo "  make pre-commit  - Run pre-commit checks"
	@echo "  make format      - Format code with ruff"
	@echo "  make clean       - Remove virtualenv and __pycache__ folders"

install:
	$(UV) venv
	$(UV) sync
	$(ACTIVATE)

lint:
	$(UV) run ruff check src
	$(UV) run black src
	$(UV) run mypy src
	$(UV) run flake8 src

pre-commit:
	$(UV) run pre-commit run --all-files

format:
	$(ACTIVATE) && ruff format src

clean:
	rm -rf $(VENV_DIR) __pycache__ **/__pycache__ .pytest_cache
