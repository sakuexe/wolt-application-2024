from main import app
from fastapi.testclient import TestClient


def test_example_order():
    """
    A test for the example order in the README
    ---
    Small order subcharge: 110
    Delivery fee: 600
    bulk charge: 0
    friday rush : 0
    ---
    Expected total: 710
    """
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
