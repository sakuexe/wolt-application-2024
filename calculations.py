from math import ceil


def small_order_surcharge(cart_value: int) -> int:
    """
    Calculate and return the small order surcharge based on the cart value.

    The value is returned in cents.
    """
    return max(0, 1000 - cart_value)


def delivery_fee(distance: int) -> int:
    """
    Calculate and return the delivery fee based on the delivery distance.

    distance: The delivery distance. (in meters)

    The value is returned in cents.
    """
    BASE_FEE: int = 200
    ADDITIONAL_FEE: int = 100

    additional_fees: int = ceil((distance - 1000) / 500)
    if additional_fees < 0:
        additional_fees = 0
    return BASE_FEE + additional_fees * ADDITIONAL_FEE


def items_fee(number_of_items: int) -> int:
    """
    Calculate and return the total fee based on the number of items.
    the total includes a bulk fee for orders with more than 12 items.

    The value is returned in cents.
    """
    SURCHARGE = 50
    BULK_FEE: int = 120

    if number_of_items < 5:
        return 0

    item_surcharge: int = SURCHARGE * (number_of_items - 4)

    if number_of_items >= 12:
        return item_surcharge + BULK_FEE

    return item_surcharge
