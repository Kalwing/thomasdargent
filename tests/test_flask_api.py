import pytest
import json
import bs4
import datetime
from flask_app.app import create_app
from flask_app.routes_api import date_match, pick_quote

@pytest.fixture
def client():
    app = create_app('dev')
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_base(client):
    response = client.get('/')
    assert response.status_code == 200


def test_brevo(client):
    response = client.get('/error_brevo')
    assert response.status_code >= 400
    assert response.json == {'code': 'error_access'}

    response = client.get('/success_brevo')
    assert response.status_code == 200
    assert b'<!doctype html>' in response.data


def test_quote(client):
    response = client.get('/get_quote')
    assert response.status_code == 200
    keys = response.json["lines"][0].keys()
    assert "author" in keys and "quote" in keys

    response = client.get('/get_quote/basic')
    assert response.status_code == 200
    keys = response.json["lines"][0].keys()
    assert "author" in keys and "quote" in keys
    assert "tag" not in response.json

    response = client.get('/get_quote/sqefsefsef')
    assert response.status_code == 404

def test_quote_date(client):
    response = client.get('/get_quote/date')
    assert response.status_code == 200
    keys = response.json["lines"][0].keys()
    assert "author" in keys and "quote" in keys

    quote = pick_quote("date", date_freq=1)
    assert "author" in quote['lines'][0] and "quote" in quote['lines'][0]

def test_date(client):
    patterns = [
        "* */*/*",
        "3 05/12/2024",
        "3 */12/*",
        "* 05/*/2024",
        "* 05/12/*",
        "* 5/12/2024"
    ]
    date1 = datetime.date(2024, 12, 5)
    date2 = datetime.date(2023, 12, 5)
    date3 = datetime.date(2024, 12, 19)

    date1_match = [date_match(date1, pattern) for pattern in patterns]
    assert date1_match == [True, True, True, True, True, False]
    date2_match = [date_match(date2, pattern) for pattern in patterns]
    assert date2_match == [True, False, False, False, True, False]
    date3_match = [date_match(date3, pattern) for pattern in patterns]
    assert date3_match == [True, False, True, False, False, False]