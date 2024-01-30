from fastapi.testclient import TestClient
from main import app

"""
Test the validation logic.
Cart value and number of items must be positive integers.
Time must be in ISO format and in UTC timezone.
"""


def test_invalid_cart_value():
    # negative cart value
    request = {
        "cart_value": -1,
        "delivery_distance": 1000,
        "number_of_items": 1,
        "time": "2024-01-15T13:00:00Z"
    }
    client = TestClient(app)
    response = client.post(
        "/", headers={"Content-Type": "application/json"}, json=request)
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid input. Reason: `cart_value` is negative"
    }


def test_invalid_number_of_items():
    # negative number of items
    request = {
        "cart_value": 1000,
        "delivery_distance": 1000,
        "number_of_items": -1,
        "time": "2024-01-15T13:00:00Z"
    }
    client = TestClient(app)
    response = client.post(
        "/", headers={"Content-Type": "application/json"}, json=request)
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid input. Reason: `number_of_items` is negative"
    }


def test_invalid_time_format():
    # test for non-ISO format
    request = {
        "cart_value": 1000,
        "delivery_distance": 1000,
        "number_of_items": 1,
        "time": "15-01-2024 13:00:00"
    }
    client = TestClient(app)
    response = client.post(
        "/", headers={"Content-Type": "application/json"}, json=request)
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid input. Reason: `time` is not in ISO format"
    }


def test_invalid_timezone():
    # test for non-UTC timezone
    request = {
        "cart_value": 1000,
        "delivery_distance": 1000,
        "number_of_items": 1,
        "time": "2021-01-01T00:00:00"
    }
    client = TestClient(app)
    response = client.post(
        "/", headers={"Content-Type": "application/json"}, json=request)
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid input. Reason: `time` is not in UTC timezone"
    }
