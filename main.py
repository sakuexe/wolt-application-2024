from fastapi import FastAPI
from pydantic import BaseModel

from calculations import surcharge, delivery_fee


class Order(BaseModel):
    # fastapi will validate the request body against this schema
    cart_value: int
    delivery_distance: int
    number_of_items: int
    time: str


app = FastAPI()


@app.post("/")
def root(order: Order):
    fees = 0  # in cents
    fees += surcharge(order.cart_value)
    fees += delivery_fee(order.delivery_distance)
    return order, fees
