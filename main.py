from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from calculations import small_order_surcharge, distance_fee, items_fee, rush_hour_fee
from validate import validate_request


class Order(BaseModel):
    # fastapi will validate the request body against this schema
    cart_value: int
    delivery_distance: int
    number_of_items: int
    time: str


app = FastAPI()


@app.post("/")
def root(order: Order):
    validate_request(order)

    # free delivery for orders over 200 euros (20000 cents)
    if order.cart_value >= 20000:
        return {"delivery_fee": 0}

    try:
        fees = 0  # in cents
        fees += small_order_surcharge(order.cart_value)
        fees += distance_fee(order.delivery_distance)
        fees += items_fee(order.number_of_items)
        fees += rush_hour_fee(order.time, fees)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Internal server error - {e}")

    # the delivery fee can NEVER be more than 15 euros (1500 cents)
    return {"delivery_fee": min(fees, 1500)}
