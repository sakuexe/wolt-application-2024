def subcharge(cart_value: int) -> int:
    """
    Calculate the cart value based on the request.
    The value is in cents.
    param request: The raw cart value.
    return: The calculated cart value.
    """
    return max(0, 1000 - cart_value)
