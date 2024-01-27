# Wolt Summer 2024 Engineering Internship Application

Created by: Saku Karttunen (22.01.-31.01.2024)

## Assignment

The assignment was to create a simple HTTP API Endpoint that calculates the delivery fee for an order.
I used Python for this assignment and some fraweworks that I list below.

The API is a single POST endpoint that takes in a JSON object as a request body and returns a JSON object as a response.

The original assignment is in it's [original repository](https://github.com/woltapp/engineering-internship-2024).

## Used Technologies

- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [pytest](https://docs.pytest.org/en/6.2.x/)

## How to run

1. Enter the virtual environment

```bash
# Linux / macOS
source venv/bin/activate
# Windows
venv\Scripts\activate.bat
```

2. Install the dependencies

```bash
pip install -r requirements.txt
```

3. Run the server

```bash
uvicorn main:app
# the default port is 8000, but you can choose a custom one like this
uvicorn main:app --port 4321
```

4. Make a POST request to the endpoint

```bash
curl -X POST -H "Content-Type: application/json" -d '{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2024-01-15T13:00:00Z"}' http://127.0.0.1:8000
```

### How to run tests

The tests are located in the `tests` directory. I used FastAPI's `TestClient` to test the API.
and simple `pytest` compatible functions to create unit tests for all the small parts as well
as more general tests for the entirety of the API.

To run the tests, run the following command:

```bash
pytest
```