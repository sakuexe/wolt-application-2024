from calculations import small_order_surcharge
"""
Test the subcharge function.
The function takes in the cart's value and returns the surcharge in cents
"""


def test_under_base_fee():
    assert small_order_surcharge(500) == 500
    assert small_order_surcharge(1) == 999


def test_over_base_fee():
    assert small_order_surcharge(1000) == 0
    assert small_order_surcharge(1001) == 0
    assert small_order_surcharge(100000001) == 0
