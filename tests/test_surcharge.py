from calculations import surcharge
"""
Test the subcharge function.
The function takes in the cart's value and returns the surcharge in cents
"""


def test_under_base_fee():
    assert surcharge(500) == 500
    assert surcharge(1) == 999


def test_over_base_fee():
    assert surcharge(1000) == 0
    assert surcharge(1001) == 0
    assert surcharge(100000001) == 0
