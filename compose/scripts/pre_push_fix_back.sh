#!/bin/bash

set +e

SOURCE=$(basename "${BASH_SOURCE[0]}")
SOURCE_DIR=$(dirname "${BASH_SOURCE[0]}")

source "$SOURCE_DIR/utils.sh"

echo ""

# Check all files and fix them when it is possible
no_log_if_successful flake8 .
no_log_if_successful isort . --profile black
no_log_if_successful black .

# Make migrations
no_log_if_successful python manage.py makemigrations
