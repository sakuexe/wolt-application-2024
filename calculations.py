from math import ceil
from datetime import datetime
import math


def small_order_surcharge(cart_value: int) -> int:
    """
    Calculate and return the small order surcharge based on the cart value.

    The value is returned in cents.
    """
    MIN_CART_VALUE: int = 1000

    return max(0, MIN_CART_VALUE - cart_value)


def distance_fee(distance: int) -> int:
    """
    Calculate and return the delivery fee based on the delivery distance.
    (in meters)

    The value is returned in cents.
    """
    BASE_FEE: int = 200
    ADDITIONAL_FEE: int = 100

    additional_fees: int = ceil((abs(distance) - 1000) / 500)
    if additional_fees < 0:
        additional_fees = 0
    return BASE_FEE + additional_fees * ADDITIONAL_FEE


def items_fee(number_of_items: int) -> int:
    """
    Calculate and return the total fee based on the number of items.
    the total includes a bulk fee for orders with more than 12 items.

    The value is returned in cents.
    """
    SURCHARGE: int = 50
    BULK_FEE: int = 120
    # the minimum amount of items needed for the surcharge to apply
    MIN_FEE_ITEMS: int = 5
    # the amount of items needed for the bulk fee to apply
    MIN_BULK_ITEMS: int = 12

    if number_of_items < MIN_FEE_ITEMS:
        return 0

    item_surcharge: int = SURCHARGE * (number_of_items - (MIN_FEE_ITEMS - 1))

    if number_of_items >= MIN_BULK_ITEMS:
        return item_surcharge + BULK_FEE

    return item_surcharge


def rush_hour_fee(iso_time: str, current_fee) -> int:
    """
    Calculate and return the rush hour fee based on the time of the order.
    If the order is placed between 3pm and 7pm on a Friday, the fee is +20%
    to the total order value.

    The time is sent in ISO format and UTC timezone (YYYY-MM-DDTHH:MM:SSZ).

    The value is returned in cents.
    """

    ORDER_TIME = datetime.fromisoformat(iso_time)
    RUSH_HOUR_FEE = current_fee * 0.2

    # don't apply if the order is not placed on a Friday
    # Monday == 0 ... Sunday == 6
    if ORDER_TIME.weekday() != 4:
        return 0

    # don't apply if the order is placed before 3:00pm
    if ORDER_TIME.hour < 15:
        return 0

    # don't apply if the order is placed after 7:00pm
    if ORDER_TIME.hour >= 19:
        return 0

    # if the checks pass return the rush hour fee
    # rounds the fee up to the nearest cent (no subcents)
    return math.ceil(RUSH_HOUR_FEE)
