from main import app
from fastapi.testclient import TestClient


def test_example_order():
    # A test for the example order in the README
    client = TestClient(app)
    response = client.post(
        "/",
        headers={"Conent-Type": "application/json"},
        json={"cart_value": 790, "delivery_distance": 2235,
              "number_of_items": 4, "time": "2024-01-15T13:00:00Z"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "delivery_fee": 710
    }


def test_no_cart_value():
    # Test for when no cart_value is given
    client = TestClient(app)
    response = client.post(
        "/",
        headers={"Conent-Type": "application/json"},
        json={"delivery_distance": 2235,
              "number_of_items": 4, "time": "2024-01-15T13:00:00Z"}
    )
    assert response.status_code == 422


def test_no_delivery_distance():
    # Test for when no delivery_distance is given
    client = TestClient(app)
    response = client.post(
        "/",
        headers={"Conent-Type": "application/json"},
        json={"cart_value": 790,
              "number_of_items": 4, "time": "2024-01-15T13:00:00Z"}
    )
    assert response.status_code == 422


def test_no_number_of_items():
    # Test for when no number_of_items is given
    client = TestClient(app)
    response = client.post(
        "/",
        headers={"Conent-Type": "application/json"},
        json={"cart_value": 790, "delivery_distance": 2235,
              "time": "2024-01-15T13:00:00Z"}
    )
    assert response.status_code == 422


def test_no_time():
    # Test for when no time is given
    client = TestClient(app)
    response = client.post(
        "/",
        headers={"Conent-Type": "application/json"},
        json={"cart_value": 790, "delivery_distance": 2235,
              "number_of_items": 4}
    )
    assert response.status_code == 422
