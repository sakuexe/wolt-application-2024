#!/bin/python3.11

import random
from requests import post
from datetime import datetime
from calculations import rush_hour_fee
import sys
from time import sleep

"""
This script generates random orders and sends them to the API.
It is made to be used to test and review the API.
"""

ORDER_INTERVAL = 3  # Seconds between orders
NUMBER_OF_ORDERS = 10  # Number of orders to generate

api_url = "http://localhost:8000/"
if len(sys.argv) > 1 and sys.argv[1] == "--container":
    api_url = "http://wolt-api:8000/"


def random_order() -> None:
    cart_value = random.randint(500, 24000)
    delivery_distance = random.randint(200, 5000)
    number_of_items = random.randint(1, 20)
    random_day = random.randint(22, 29)
    time = f"2024-01-{random_day}T16:00:00.00Z"

    body = {
        "cart_value": cart_value,
        "delivery_distance": delivery_distance,
        "number_of_items": number_of_items,
        "time": time
    }

    print("Request body:")
    print(body)
    if rush_hour_fee(time, cart_value):
        print("Friday rush")

    response = post(api_url, json=body).json()
    sleep(0.2)  # To avoid mixing up the docker logs
    print("Response body:")
    print(response)


if len(sys.argv) > 1 and sys.argv[1] == "--container":
    for i in range(NUMBER_OF_ORDERS):
        random_order()
        sleep(ORDER_INTERVAL)
else:
    random_order()
