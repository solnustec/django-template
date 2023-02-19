help:
	@grep -E '^[A-Za-z0-9_.-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "[36m%-30s[0m %s\n", $$1, $$2}'

#
# Setup commands
#
run-tests:  ## Equivalent to python manage.py test --settings=tests.settings
	pytest -n auto --reuse-db --no-migrations --vcr-record-mode=none --durations=30 --cov --cov-report=

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

pre-push-fix-back:  ## Fix most of backend conflicts
	./compose/scripts/pre_push_fix_back.sh


pre-push-back:  ## Check backend code
	./compose/scripts/pre_push_back.sh
