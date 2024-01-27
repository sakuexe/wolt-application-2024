from fastapi.testclient import TestClient
from main import app


def test_invalid_cart_value():
    request = {
        "cart_value": -1,
        "delivery_distance": 1000,
        "number_of_items": 1,
        "time": "2024-01-15T13:00:00Z"
    }
    client = TestClient(app)
    response = client.post(
        "/", headers={"Conent-Type": "application/json"}, json=request)
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid input. Reason: `cart_value` is negative"
    }


def test_invalid_number_of_items():
    request = {
        "cart_value": 1000,
        "delivery_distance": 1000,
        "number_of_items": -1,
        "time": "2024-01-15T13:00:00Z"
    }
    client = TestClient(app)
    response = client.post(
        "/", headers={"Conent-Type": "application/json"}, json=request)
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid input. Reason: `number_of_items` is negative"
    }


def test_invalid_time_format():
    request = {
        "cart_value": 1000,
        "delivery_distance": 1000,
        "number_of_items": 1,
        "time": "15-01-2024 13:00:00"
    }
    client = TestClient(app)
    response = client.post(
        "/", headers={"Conent-Type": "application/json"}, json=request)
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid input. Reason: `time` is not in ISO format"
    }


def test_invalid_timezone():
    request = {
        "cart_value": 1000,
        "delivery_distance": 1000,
        "number_of_items": 1,
        "time": "2021-01-01T00:00:00"
    }
    client = TestClient(app)
    response = client.post(
        "/", headers={"Conent-Type": "application/json"}, json=request)
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid input. Reason: `time` is not in UTC timezone"
    }