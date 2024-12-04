import pytest
from flask_app.app import create_app

@pytest.fixture
def client():
    app = create_app('prod')
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_page_brevo(client):
    response = client.get('api/brevo_form_example')
    assert response.status_code == 200
    assert b'htmx' not in response.data

    response = client.get('api/brevo_success_example')
    assert response.status_code == 200
    assert b'/success_brevo' in response.data

    response = client.get('api/brevo_error_example')
    assert response.status_code == 200
    assert b'/error_brevo' in response.data


def test_page_mass_effect(client):
    response = client.get('api/mass_effect_quote')
    assert response.status_code == 200
    assert b'quote' in response.data


def test_page_wisdom(client):
    response = client.get('api/wisdom')
    assert response.status_code == 200
    assert b'quote' in response.data