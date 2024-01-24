from math import ceil


def surcharge(cart_value: int) -> int:
    """
    Calculate the cart value based on the cart value.
    The value is in cents.
    param request: The raw cart value.
    return: The calculated cart value.
    """
    return max(0, 1000 - cart_value)


def delivery_fee(distance: int) -> int:
    """
    Calculate the delivery fee based on the delivery distance.
    The value is in meters.
    param distance: The delivery distance.
    return: The calculated delivery fee.
    """
    base_fee: int = 200
    additional_fees: int = ceil((distance - 1000) / 500)
    if additional_fees < 0:
        additional_fees = 0
    return base_fee + additional_fees * 100


def items_fee(number_of_items: int) -> int:
    """
    Calculate the surcharge and possible bulk fee based on the number of items.
    param number_of_items: The number of items.
    return: The combined surcharge and bulk fee.
    """
    if number_of_items < 5:
        return 0

    item_surcharge: int = (number_of_items - 4) * 50

    if number_of_items >= 12:
        return item_surcharge + 120

    return item_surcharge
