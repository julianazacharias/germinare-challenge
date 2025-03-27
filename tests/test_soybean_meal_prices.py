from decimal import Decimal
from http import HTTPStatus

from desafio_germinare.database.models import SoybeanMealPrice

EXPECTED_BASIS = -5.00
EXPECTED_CBOT_PRICE_MAY24 = 450.00
EXPECTED_FLAT_PRICE_MAY24 = 490.53
EXPECTED_CBOT_PRICE_JUL24 = 460.00
EXPECTED_FLAT_PRICE_JUL24 = 501.55


def test_create_soybean_meal_price(client):
    response = client.post(
        '/api/',
        json={
            'contract_month': 'MAY24',
            'price': 450.00,
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'contract_month': 'MAY24',
        'price': 450.00,
    }


def test_delete_soybean_meal_price(client, soybean_meal_price):
    response = client.delete(
        f'/api/{soybean_meal_price.id}',
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'message': 'Soybean Meal Price has been deleted successfully.'
    }


def test_delete_soybean_meal_price_error(client):
    response = client.delete(
        f'/api/{10}',
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Soybean Meal Price not found'}


def test_patch_soybean_meal_price(client, soybean_meal_price):
    response = client.patch(
        f'/api/{soybean_meal_price.id}',
        json={'contract_month': 'JUL24'},
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json()['contract_month'] == 'JUL24'


def test_patch_soybean_meal_pric_error(client):
    response = client.patch(
        f'/api/{10}',
        json={'contract_month': 'FEB24'},
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Soybean Meal Price not found'}


def test_get_flat_prices(client, session):
    soybean_meal_price_may24 = SoybeanMealPrice(
        contract_month='MAY24', price=Decimal('450.00')
    )
    soybean_meal_price_jul24 = SoybeanMealPrice(
        contract_month='JUL24', price=Decimal('460.00')
    )

    session.add(soybean_meal_price_may24)
    session.add(soybean_meal_price_jul24)
    session.commit()

    flat_price_request = {
        'contract_months': ['MAY24', 'JUL24'],
        'basis': EXPECTED_BASIS,
    }

    response = client.post('/api/flat_price', json=flat_price_request)

    data = response.json()

    assert response.status_code == HTTPStatus.CREATED

    assert 'results' in data

    may24_result = data['results'][0]
    assert may24_result['contract_month'] == 'MAY24'
    assert float(may24_result['cbot_price']) == EXPECTED_CBOT_PRICE_MAY24
    assert float(may24_result['flat_price']) == EXPECTED_FLAT_PRICE_MAY24

    jul24_result = data['results'][1]
    assert jul24_result['contract_month'] == 'JUL24'
    assert float(jul24_result['cbot_price']) == EXPECTED_CBOT_PRICE_JUL24
    assert float(jul24_result['flat_price']) == EXPECTED_FLAT_PRICE_JUL24
