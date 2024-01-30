from main import app
from fastapi.testclient import TestClient
"""
Test cases for the entire API in case of a valid request.
"""


def test_example_order():
    """
    A test for the example order in the README
    ---
    Small order subcharge: 110 (1000 - 890)
    Delivery fee: 600 (200 + 100 * 4)
    bulk charge: 0
    friday rush fee: 0
    """
    EXPECTED_TOTAL = 710
    order = {
        "cart_value": 790,
        "delivery_distance": 2235,
        "number_of_items": 4,
        "time": "2024-01-15T13:00:00Z"
    }

    client = TestClient(app)
    response = client.post(
        "/", headers={"Content-Type": "application/json"}, json=order)

    assert response.status_code == 200
    assert response.json() == {
        "delivery_fee": EXPECTED_TOTAL
    }


def test_small_order():
    """
    Small order subcharge: 500 (1000 - 500)
    Delivery fee: 200 (200 + 100 * 0)
    bulk charge: 0
    friday rush fee: 0
    """
    EXPECTED_TOTAL = 700
    order = {
        "cart_value": 500,
        "delivery_distance": 972,
        "number_of_items": 1,
        "time": "2024-01-15T13:00:00Z"
    }

    client = TestClient(app)
    response = client.post(
        "/", headers={"Content-Type": "application/json"}, json=order)

    assert response.status_code == 200
    assert response.json() == {
        "delivery_fee": EXPECTED_TOTAL
    }


def test_bulk_order():
    """
    Small order subcharge: 0
    Delivery fee: 400 (200 + 100 * 2)
    bulk charge: 520 (8 * 50 + 120)
    friday rush fee: 0
    """
    EXPECTED_TOTAL = 920
    order = {
        "cart_value": 1200,
        "delivery_distance": 1501,
        "number_of_items": 12,
        "time": "2024-01-15T13:00:00Z"
    }

    client = TestClient(app)
    response = client.post(
        "/", headers={"Content-Type": "application/json"}, json=order)

    assert response.status_code == 200
    assert response.json() == {
        "delivery_fee": EXPECTED_TOTAL
    }


def test_rush_hour():
    """
    Small order subcharge: 0
    Delivery fee: 300 (200 + 100 * 1)
    bulk charge: 0
    friday rush fee: 60 (20% of 300)
    """
    EXPECTED_TOTAL = 360
    order = {
        "cart_value": 1200,
        "delivery_distance": 1500,
        "number_of_items": 2,
        "time": "2024-01-19T15:00:50Z"
    }

    client = TestClient(app)
    response = client.post(
        "/",
        headers={"Content-Type": "application/json"},
        json=order
    )

    assert response.status_code == 200
    assert response.json() == {
        "delivery_fee": EXPECTED_TOTAL
    }


def test_all_fees():
    """
    Small order subcharge: 280 (1000 - 720)
    Delivery fee: 500 (200 + 100 * 3)
    bulk charge: 100 (50 * 2)
    friday rush fee: 176 (20% of 880)
    """
    EXPECTED_TOTAL = 1056
    order = {
        "cart_value": 720,
        "delivery_distance": 2500,
        "number_of_items": 6,
        "time": "2024-01-19T18:59:50Z"
    }

    client = TestClient(app)
    response = client.post(
        "/",
        headers={"Content-Type": "application/json"},
        json=order
    )

    assert response.status_code == 200
    assert response.json() == {
        "delivery_fee": EXPECTED_TOTAL
    }
