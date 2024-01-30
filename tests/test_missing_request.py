from main import app
from fastapi.testclient import TestClient
"""
Test cases for the entire API in case of missing parameters.
"""


def test_no_cart_value():
    # Test for when no cart_value is given
    order = {
        "delivery_distance": 2235,
        "number_of_items": 4,
        "time": "2024-01-15T13:00:00Z"
    }
    client = TestClient(app)
    response = client.post(
        "/", headers={"Content-Type": "application/json"}, json=order)
    assert response.status_code == 422


def test_no_delivery_distance():
    # Test for when no delivery_distance is given
    order = {
        "cart_value": 790,
        "number_of_items": 4,
        "time": "2024-01-15T13:00:00Z"
    }
    client = TestClient(app)
    response = client.post(
        "/", headers={"Content-Type": "application/json"}, json=order)
    assert response.status_code == 422


def test_no_number_of_items():
    # Test for when no number_of_items is given
    order = {
        "cart_value": 790,
        "delivery_distance": 2235,
        "time": "2024-01-15T13:00:00Z"
    }
    client = TestClient(app)
    response = client.post(
        "/", headers={"Content-Type": "application/json"}, json=order)
    assert response.status_code == 422


def test_no_time():
    order = {
        "cart_value": 790,
        "delivery_distance": 2235,
        "number_of_items": 4,
    }
    client = TestClient(app)
    response = client.post(
        "/", headers={"Content-Type": "application/json"}, json=order)
    assert response.status_code == 422
