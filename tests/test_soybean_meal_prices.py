from http import HTTPStatus

EXPECTED_RESULTS_LENGTH = 2
EXPECTED_CBOT_PRICE_MAY24 = 450.00
EXPECTED_BASIS_MAY24 = -5.00
EXPECTED_FLAT_PRICE_MAY24 = 490.53
EXPECTED_CBOT_PRICE_JUL24 = 460.00
EXPECTED_BASIS_JUL24 = -5.00
EXPECTED_FLAT_PRICE_JUL24 = 501.55


def test_create_soybean_meal_price(client):
    response = client.post(
        '/api/',
        json={
            'contract_month': 'MAY24',
            'price': 480.00,
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'contract_month': 'MAY24',
        'price': 480.00,
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
        json={'contract_month': 'AUG24'},
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json()['contract_month'] == 'AUG24'


def test_patch_soybean_meal_pric_error(client):
    response = client.patch(
        f'/api/{10}',
        json={'contract_month': 'FEB24'},
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Soybean Meal Price not found'}


def test_get_soybean_meal_price_by_id(client, soybean_meal_price):
    response = client.get(
        f'/api/{soybean_meal_price.id}',
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'contract_month': 'MAR24',
        'price': 450.00,
    }


def test_get_soybean_meal_price_by_id_error(client):
    response = client.get(f'/api/{9999}')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Soybean Meal Price not found'}


def test_get_flat_prices(client):
    flat_price_request = {
        'contract_months': ['MAY24', 'JUL24'],
        'basis': EXPECTED_BASIS_MAY24,
    }

    response = client.post('/api/flat_price/', json=flat_price_request)

    assert response.status_code == HTTPStatus.CREATED

    assert response.json() == {
        'results': [
            {
                'contract_month': 'MAY24',
                'cbot_price': EXPECTED_CBOT_PRICE_MAY24,
                'basis': EXPECTED_BASIS_MAY24,
                'flat_price': EXPECTED_FLAT_PRICE_MAY24,
            },
            {
                'contract_month': 'JUL24',
                'cbot_price': EXPECTED_CBOT_PRICE_JUL24,
                'basis': EXPECTED_BASIS_JUL24,
                'flat_price': EXPECTED_FLAT_PRICE_JUL24,
            },
        ]
    }
