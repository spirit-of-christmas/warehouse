.PHONY: env clean start stop build test requires lint docs migrate migrations createsuperuser logs
.DEFAULT: env

env:
	@python -m venv .venv
	@poetry install

clean:
	@rm -rf .venv
	@rm -rf poetry.lock
	@rm -rf requirements.txt
	@rm -rf requirements-dev.txt

start:
	@docker-compose up -d

stop:
	@docker container stop warehouse_web_1
	@docker container rm warehouse_web_1
	@docker container stop warehouse_database_1
	@docker container rm warehouse_database_1

build:
	@docker-compose build

logs:
	@docker logs --follow warehouse_web_1

test:
	@docker exec -it warehouse_web_1 coverage run --branch -m unittest discover --pattern=tests/*.py
	@docker exec -it warehouse_web_1 coverage html

requires:
	@poetry export -f requirements.txt --output requirements.txt --without-hashes

requires-dev:
	@poetry export --dev -f requirements.txt --output requirements-dev.txt --without-hashes

lint:
	@docker exec -it warehouse_web_1 isort --virtual-env .venv warehouse/*.py
	@docker exec -it warehouse_web_1 black . --exclude migrations

docs:
	@docker exec -it warehouse_web_1 /bin/bash -c "sphinx-apidoc -f -o docs/source/ warehouse ./tests/*.py && cd docs && make html"

migrate:
	@docker exec -it warehouse_web_1 python manage.py migrate

migrations:
	@docker exec -it warehouse_web_1 python manage.py makemigrations

createsuperuser:
	@docker exec -it warehouse_web_1 python manage.py createsuperuser --noinput
