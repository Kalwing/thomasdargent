import pytest
import json
import bs4
from flask_app.app import create_app

@pytest.fixture
def client():
    app = create_app('prod')
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_base(client):
    response = client.get('api/')
    assert response.status_code == 200


def test_brevo(client):
    response = client.get('api/error_brevo')
    assert response.status_code >= 400
    assert response.json == {'code': 'error_access'}

    response = client.get('api/success_brevo')
    assert response.status_code == 200
    assert b'<!doctype html>' in response.data


def test_quote(client):
    response = client.get('api/get_quote')
    assert response.status_code == 200
    keys = response.json["lines"][0].keys()
    assert "author" in keys and "quote" in keys

    response = client.get('api/get_quote/basic')
    assert response.status_code == 200
    keys = response.json["lines"][0].keys()
    assert "author" in keys and "quote" in keys