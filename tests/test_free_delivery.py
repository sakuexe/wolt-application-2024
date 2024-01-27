from fastapi.testclient import TestClient
from main import app


def test_free_delivery():
    """
    Small order subcharge: 0
    Delivery fee: 700 (200 + 100 * 5)
    bulk charge: 670 (50 * 11 + 120)
    friday rush fee: 0
    cart value is over 200 euros, so delivery is free
    ---
    Expected total: 0
    """
    client = TestClient(app)
    response = client.post(
        "/",
        headers={"Conent-Type": "application/json"},
        json={"cart_value": 20000, "delivery_distance": 3821,
              "number_of_items": 15, "time": "2024-01-19T18:59:50Z"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "delivery_fee": 0
    }


def test_over_maximum():
    """
    Small order subcharge: 0
    Delivery fee: 900 (200 + 100 * 7)
    bulk charge: 670 (50 * 11 + 120)
    friday rush fee: 0
    total is 1570 cents, so delivery is capped at 15 euros
    ---
    Expected total: 1500
    """
    client = TestClient(app)
    response = client.post(
        "/",
        headers={"Conent-Type": "application/json"},
        json={"cart_value": 3500, "delivery_distance": 4501,
              "number_of_items": 15, "time": "2024-01-19T18:59:50Z"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "delivery_fee": 1500
    }
