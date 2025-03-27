# Germinare Challenge

A simple API built for Germinare Challenge

## How to run the project

### Test with Swagger

- [Path to Swagger URL to test locally](http://localhost:8000/docs)

### Requirements

- [Python](https://www.python.org/) ^3.12
- [Poetry](https://python-poetry.org/) 1.8.3

### With poetry

1. Install the dependencies:

```bash
poetry install
```

2. Activate the virtual environment:

```bash
poetry shell
```

3. Run the application:

```bash
task run
```

4. Run the tests:

```bash
task test
```

5. All "task" commands:

- lint = 'ruff check .; ruff check . --diff'
- format = 'ruff check . --fix; ruff format .'
- run = 'fastapi dev desafio_germinare/app.py'
- pre_test = 'task lint'
- test = 'pytest -s -x --cov=desafio_germinare -vv'
- post_test = 'coverage html'

### With Docker

1. Build the image:

```bash
docker-compose build
```

2. Run the application:

```bash
docker-compose up
```

### .ENV file:

Insert your API KEY value on **.env** file:

- DATABASE_URL=""
- CONVERSION_FACTOR=""
- BASIS_THRESHOLD=""

## Everything used in this project

- [Python 3.12](https://www.python.org/) as the programming language.
- [Poetry](https://python-poetry.org/) to manage dependencies.
- [FastAPI](https://fastapi.tiangolo.com/) as the framework
- [SQLAlchemy](https://www.sqlalchemy.org/) for database management.
- [Pydantic](https://pydantic-docs.helpmanual.io/) for validating and converting Data-Transfer-Objects and database models.
- [Alembic](https://alembic.sqlalchemy.org/en/latest/) for database migrations.
- [PostgreSQL](https://www.postgresql.org/) as the database.
- [Docker](https://www.docker.com/) for containerization.
- [Docker Compose](https://docs.docker.com/compose/) for managing containers.
