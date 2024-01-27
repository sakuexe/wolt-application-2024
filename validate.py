from datetime import datetime
from fastapi import HTTPException


def validate_request(order):
    # The delivery distance isn't validated, as it is used as an absolute value

    if order.cart_value < 0:
        raise HTTPException(
            status_code=400,
            detail="Invalid input. Reason: `cart_value` is negative"
        )
    if order.number_of_items < 0:
        raise HTTPException(
            status_code=400,
            detail="Invalid input. Reason: `number_of_items` is negative"
        )

    try:
        time = datetime.fromisoformat(order.time)
        if time.tzname() != "UTC":
            raise HTTPException(
                status_code=400,
                detail="Invalid input. Reason: `time` is not in UTC timezone"
            )
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Invalid input. Reason: `time` is not in ISO format"
        )
