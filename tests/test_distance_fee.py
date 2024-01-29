from calculations import distance_fee

"""
Test the delivery_fee function.
The function takes in a distance and returns the delivery fee in cents
"""

BASE_FEE: int = 200
EXTRA_DISTANCE_FEE: int = 100


def test_under_extra_fee():
    assert distance_fee(500) == BASE_FEE
    assert distance_fee(1) == BASE_FEE
    assert distance_fee(0) == BASE_FEE
    assert distance_fee(999) == BASE_FEE
    assert distance_fee(1000) == BASE_FEE
    # negatives, since distance is considered absolute
    assert distance_fee(-1) == BASE_FEE
    assert distance_fee(-500) == BASE_FEE
    assert distance_fee(-999) == BASE_FEE


def test_over_extra_fee():
    assert distance_fee(1001) == BASE_FEE + EXTRA_DISTANCE_FEE
    assert distance_fee(1499) == BASE_FEE + EXTRA_DISTANCE_FEE
    assert distance_fee(1500) == BASE_FEE + EXTRA_DISTANCE_FEE
    assert distance_fee(1501) == BASE_FEE + EXTRA_DISTANCE_FEE * 2
    assert distance_fee(4000) == BASE_FEE + EXTRA_DISTANCE_FEE * 6
    assert distance_fee(4001) == BASE_FEE + EXTRA_DISTANCE_FEE * 7
    # negatives, since distance is considered absolute
    assert distance_fee(-1001) == BASE_FEE + EXTRA_DISTANCE_FEE
    assert distance_fee(-1499) == BASE_FEE + EXTRA_DISTANCE_FEE
    assert distance_fee(-1500) == BASE_FEE + EXTRA_DISTANCE_FEE
    assert distance_fee(-1501) == BASE_FEE + EXTRA_DISTANCE_FEE * 2
