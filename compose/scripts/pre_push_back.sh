#!/bin/bash

set -e

SOURCE=$(basename "${BASH_SOURCE[0]}")
SOURCE_DIR=$(dirname "${BASH_SOURCE[0]}")

source "$SOURCE_DIR/utils.sh"

# Check all files and fix them when it is possible
echo ""
#no_log_if_successful flake8 .
no_log_if_successful black . --check
no_log_if_successful isort . --check-only --profile black

# Check migrations
no_log_if_successful python manage.py makemigrations --dry-run --check

printf "${GREEN}Success!${RESET}\n"

# Pytest with log
echo "Running pytest ..."
pytest -x -n auto --reuse-db --no-migrations --vcr-record-mode=none --cov --cov-report=
