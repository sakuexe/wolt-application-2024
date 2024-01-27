from calculations import items_fee
"""
Test cases for calculating the bulk fee of the order.
"""

SURCHARGE: int = 50
BULK_FEE: int = 120


def test_under_items_fee():
    assert items_fee(0) == 0
    assert items_fee(1) == 0
    assert items_fee(2) == 0
    assert items_fee(3) == 0
    assert items_fee(4) == 0  # Example 1
    # wacky edge case
    assert items_fee(-1) == 0
    assert items_fee(-1234567890) == 0


def test_over_items_fee():
    assert items_fee(5) == SURCHARGE  # Example 2
    assert items_fee(6) == SURCHARGE * 2
    assert items_fee(7) == SURCHARGE * 3
    assert items_fee(10) == SURCHARGE * 6  # Example 3
    assert items_fee(12) == SURCHARGE * 8 + BULK_FEE
    assert items_fee(13) == SURCHARGE * 9 + BULK_FEE  # Example 4
    assert items_fee(14) == SURCHARGE * 10 + BULK_FEE  # Example 5
    assert items_fee(20) == SURCHARGE * 16 + BULK_FEE
    # wacky edge case
    assert items_fee(1234567890) == SURCHARGE * 1234567886 + BULK_FEE
