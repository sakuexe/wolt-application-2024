from fastapi import FastAPI
from pydantic import BaseModel

from calculations import small_order_surcharge, delivery_fee, items_fee


class Order(BaseModel):
    # fastapi will validate the request body against this schema
    cart_value: int
    delivery_distance: int
    number_of_items: int
    time: str


app = FastAPI()


@app.post("/")
def root(order: Order):
    # free delivery for orders over 200 euros (20000 cents)
    if order.cart_value >= 20000:
        return {"delivery_fee": 0}

    fees = 0  # in cents
    fees += small_order_surcharge(order.cart_value)
    fees += delivery_fee(order.delivery_distance)
    fees += items_fee(order.number_of_items)
    # TODO: add time-based fee
    # Friday rush (3pm - 7pm UTC) + 20% fee

    # the delivery fee can NEVER be more than 15 euros (1500 cents)
    return min(fees, 1500)
