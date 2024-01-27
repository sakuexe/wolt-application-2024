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

ORDER_INTERVAL = 5  # Seconds between orders

api_url = "http://localhost:8000/"
if len(sys.argv) > 1 and sys.argv[1] == "--container":
    api_url = "http://wolt-api:8000/"


def check_for_friday_rush(time: str) -> bool:
    if datetime.fromisoformat(time).weekday() != 4:
        return False
    if datetime.fromisoformat(time).hour < 15:
        return False
    if datetime.fromisoformat(time).hour >= 19:
        return False
    return True


def random_order() -> None:
    cart_value = random.randint(500, 24000)
    delivery_distance = random.randint(200, 5500)
    number_of_items = random.randint(1, 24)
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


for i in range(4):
    random_order()
    sleep(ORDER_INTERVAL)
