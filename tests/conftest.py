from decimal import Decimal

import factory
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from testcontainers.postgres import PostgresContainer

from desafio_germinare.app import app
from desafio_germinare.database.database import get_session
from desafio_germinare.database.models import SoybeanMealPrice, table_registry


@pytest.fixture
def client(session):
    def get_session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client

    app.dependency_overrides.clear()


@pytest.fixture(scope='session')
def engine():
    with PostgresContainer('postgres:16', driver='psycopg') as postgres:
        _engine = create_engine(postgres.get_connection_url())

        with _engine.begin():
            yield _engine


@pytest.fixture
def session(engine):
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session
        session.rollback()

    table_registry.metadata.drop_all(engine)


@pytest.fixture
def soybean_meal_price(session):
    soybean_meal_price = SoybeanMealPriceFactory()

    session.add(soybean_meal_price)
    session.commit()
    session.refresh(soybean_meal_price)

    return soybean_meal_price


class SoybeanMealPriceFactory(factory.Factory):
    class Meta:
        model = SoybeanMealPrice

    contract_month = factory.Sequence(
        lambda n: f'{
            [
                "JAN",
                "FEB",
                "MAR",
                "APR",
                "MAY",
                "JUN",
                "JUL",
                "AUG",
                "SEP",
                "OCT",
                "NOV",
                "DEC",
            ][n % 12]
        }24'
    )

    price = factory.Sequence(lambda n: Decimal(f'{n * 100:.2f}'))
