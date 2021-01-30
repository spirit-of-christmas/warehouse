.PHONY: env run test lint requires docs migrations migrate
.DEFAULT: env

env:
	@python -m venv .venv
	@poetry install

run:
	@poetry run python manage.py runserver

test:
	@poetry run coverage run --branch -m unittest discover --pattern=tests/*.py && poetry run coverage html

requires:
	@poetry export -f requirements.txt --output requirements.txt

lint:
	@poetry run isort --virtual-env .venv warehouse/*.py && poetry run black .

docs:
	@poetry run sphinx-apidoc -f -o docs/source/ warehouse ./tests/*.py
	@cd docs && make html

superuser:
	@poetry run python manage.py createsuperuser

migrate:
	@poetry run python manage.py migrate

migrations:
	@poetry run python manage.py makemigrations
