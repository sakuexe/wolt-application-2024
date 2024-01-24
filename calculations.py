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
