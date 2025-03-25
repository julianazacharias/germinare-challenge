from http import HTTPStatus

from fastapi.testclient import TestClient

from desafio_germinare.app import app


def test_root_deve_retornar_ok_e_hello_word():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World!'}
