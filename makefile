help:
	@grep -E '^[A-Za-z0-9_.-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "[36m%-30s[0m %s\n", $$1, $$2}'

#
# Setup commands
#
run-tests:  ## Equivalent to python manage.py test --settings=tests.settings
	pytest -n auto --reuse-db --no-migrations --durations=30 --cov=/src/apps --cov-report=term

migrations:  ## Make django migrations
	python3 manage.py makemigrations

migrate:  ## Apply django migrations
	python3 manage.py migrate

#
# Management commands
#
lint:
	black .
	isort . --profile black

lint-check:
	black . --check
	isort . --check-only --profile black
	flake8 .

#
# Run before push to github
#

pre-push-fix:  ## Fix most of backend conflicts
	./scripts/pre_push_fix.sh


pre-push:  ## Check backend code
	./scripts/pre_push.sh
