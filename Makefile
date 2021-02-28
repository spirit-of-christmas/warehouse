.PHONY: env run test lint requires docs migrations migrate
.DEFAULT: env

env:
	@python -m venv .venv
	@poetry install

run:
	@source .env; poetry run python manage.py runserver 0.0.0.0:8000

test:
	@source .env; poetry run coverage run --branch -m unittest discover --pattern=tests/*.py && poetry run coverage html

requires:
	@poetry export -f requirements.txt --output requirements.txt

lint:
	@source .env; poetry run isort --virtual-env .venv warehouse/*.py && poetry run black . --exclude migrations

gunicorn:
	@source .env; poetry run gunicorn

docs:
	@source .env; poetry run sphinx-apidoc -f -o docs/source/ warehouse ./tests/*.py
	@cd docs && make html

superuser:
	@source .env; poetry run python manage.py createsuperuser

migrate:
	@source .env; poetry run python manage.py migrate

migrations:
	@source .env; poetry run python manage.py makemigrations
