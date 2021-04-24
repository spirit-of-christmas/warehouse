.PHONY: env clean start stop build test requires lint docs superuser migrate migrations
.DEFAULT: env

env:
	@python -m venv .venv
	@poetry install

clean:
	@rm -rf .venv

start:
	@docker-compose up -d

stop:
	@docker container stop warehouse_web_1
	@docker container rm warehouse_web_1
	@docker container stop warehouse_database_1
	@docker container rm warehouse_database_1

build:
	@docker-compose build

test:
	@docker exec -it warehouse_web_1 coverage run --branch -m unittest discover --pattern=tests/*.py
	@docker exec -it warehouse_web_1 coverage html

requires:
	@poetry export --dev -f requirements.txt --output requirements.txt

lint:
	@docker exec -it warehouse_web_1 isort --virtual-env .venv warehouse/*.py
	@docker exec -it warehouse_web_1 black . --exclude migrations

docs:
	@docker exec -it warehouse_web_1 /bin/bash -c "sphinx-apidoc -f -o docs/source/ warehouse ./tests/*.py && cd docs && make html"

superuser:
	@docker exec -it warehouse_web_1 python manage.py createsuperuser

migrate: start
	@docker exec -it warehouse_web_1 python manage.py migrate

migrations:
	@docker exec -it warehouse_web_1 python manage.py makemigrations
