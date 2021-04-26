# warehouse

An inventory system for charitable organizations

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Config

You will need to create or acquire a .env file, an example is provided without example values, at a minimum the secret key and dropbox auth token will need to be created, although it is strongly advised to change the POSTGRES_* and DJANGO_* values the defaults should work.

### Installing

Setting up the project should be as simple as:

``` sh
make env
```

Warehouse uses Docker to run the project locally, there's a postgresql container and a django web container, they can be manipulated with the following commands:

``` sh
make build
make start
make stop
```

It is occasionally necessary to generate a requirements.txt or requirements-dev.txt there are commands to generate these:

``` sh
make requires
make requires-dev
```

While working with Django it will be required to make migrations, apply migrations and create a superuser, the following commands exist for this purpose.

``` sh
make makemigrations
make migrate
make createsuperuser
```

### Running the tests

``` sh
make tests
```

### Linting code

``` sh
make lint
```

### Generating the documentation

``` sh
make docs
```

## Authors

* NMunro (neilmunro@gmail.com)

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

