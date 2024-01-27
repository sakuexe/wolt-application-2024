from calculations import distance_fee

"""
Test the delivery_fee function.
The function takes in a distance and returns the delivery fee in cents
"""

BASE_FEE: int = 200


def test_under_extra_fee():
    assert distance_fee(500) == BASE_FEE
    assert distance_fee(1) == BASE_FEE
    assert distance_fee(0) == BASE_FEE
    assert distance_fee(999) == BASE_FEE
    assert distance_fee(1000) == BASE_FEE


def test_over_extra_fee():
    assert distance_fee(1001) == 300
    assert distance_fee(1499) == 300
    assert distance_fee(1500) == 300
    assert distance_fee(1501) == 400
