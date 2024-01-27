from datetime import datetime


def validate_request(order) -> str:

    # no negative values
    if order.cart_value < 0:
        return "`cart_value` is negative"
    if order.delivery_distance < 0:
        return "`delivery_distance` is negative"
    if order.number_of_items < 0:
        return "`number_of_items` is negative"

    # time must be in iso format and in UTC
    try:
        time = datetime.fromisoformat(order.time)
        if time.tzname() != "UTC":
            return "`time` is not in UTC"
    except ValueError:
        return "`time` is not in iso format"

    return ""
