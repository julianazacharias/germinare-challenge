# Germinare Challenge

A simple API built for Germinare Challenge

## Como rodar o projeto

### Teste com o Swagger

- [URL para acessar o swagger ao testar localmente](http://localhost:8000/docs)

### Requisitos

- [Python](https://www.python.org/) ^3.12
- [Poetry](https://python-poetry.org/) 1.8.3

### Com poetry

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

5. Todos os comandos do "task" (taskipy):

- task lint = 'ruff check .; ruff check . --diff'
- task format = 'ruff check . --fix; ruff format .'
- task run = 'fastapi dev desafio_germinare/app.py'
- task pre_test = 'task lint'
- task test = 'pytest -s -x --cov=desafio_germinare -vv'
- task post_test = 'coverage html'

### Com docker

1. Build the image:

```bash
docker-compose build
```

2. Run the application:

```bash
docker-compose up
```

Ao rodar o docker compose, as migrations devem rodar automaticamente

### Com docker localmente

Caso não queira usar o docker compose, você pode testar com o Docker localmente:

```bash
docker run -d \
    --name app_database \
    -e POSTGRES_USER=app_user \
    -e POSTGRES_DB=app_db \
    -e POSTGRES_PASSWORD=app_password \
    -v pgdata:/var/lib/postgresql/data \
    -p 5432:5432 \
    postgres
```

Para aplicar as migrações:

```bash
alembic upgrade head
```

Para aplicar migrações em um ambiente com contêineres:

```bash
docker exec -it germinare_challenge poetry run alembic upgrade head
```

### O arquivo .ENV

Insira suas chaves no arquivo **.env**:

- DATABASE_URL=""
- CONVERSION_FACTOR=""
- BASIS_THRESHOLD=""

Há um arquivo .env.example pronto com os valores já inseridos para te auxiliar com isso

## Tudo que usei nesse projeto

- [Python 3.12](https://www.python.org/) as the programming language.
- [Poetry](https://python-poetry.org/) to manage dependencies.
- [FastAPI](https://fastapi.tiangolo.com/) as the framework
- [SQLAlchemy](https://www.sqlalchemy.org/) for database management.
- [Pydantic](https://pydantic-docs.helpmanual.io/) for validating and converting Data-Transfer-Objects and database models.
- [Alembic](https://alembic.sqlalchemy.org/en/latest/) for database migrations.
- [PostgreSQL](https://www.postgresql.org/) as the database.
- [Docker](https://www.docker.com/) for containerization.
- [Docker Compose](https://docs.docker.com/compose/) for managing containers.
