# Wolt Summer 2024 Engineering Internship Application

Created by: Saku Karttunen (22.01.-31.01.2024)

## Assignment

The assignment was to create a simple HTTP API Endpoint that calculates the delivery fee for an order.
I used Python for this assignment and some fraweworks that I list below.

The API is a single POST endpoint that takes in a JSON object as a request body and returns a JSON object as a response.

The original assignment is in it's [original repository](https://github.com/woltapp/engineering-internship-2024).

## Used Technologies

- [Python 3.11](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/) - A Python framework for creating APIs
- [Uvicorn](https://www.uvicorn.org/) - For running the API
- [pytest](https://docs.pytest.org/en/6.2.x/) - For testing the API
- [Docker](https://www.docker.com/) - For containerizing the API
- [Requests](https://docs.python-requests.org/en/latest/) - For making randomized requests to the API

## How to run

### Docker

1. Run docker compose

```bash
docker-compose up
# or if you want to run it in the background
docker-compose up -d
```

The container has the port `8000` exposed, so you can access it from `localhost:8000`.

I added a fake client that makes randomized order requests to the API.
So you can just run the program and see the results. This "client"
only makes 5 orders and then stops.

Once the container is running. You can make more requests to the
endpoint with `curl` or the `fake_client.py` script.

### Manually

1. Enter the virtual environment

```bash
# Linux / macOS
source venv/bin/activate
# Windows
.\venv\Scripts\activate.ps1
```

2. Install the dependencies

```bash
pip install -r requirements.txt
```

3. Run the server

```bash
uvicorn main:app
```

4. Make a POST request to the endpoint

```bash
curl -X POST -H "Content-Type: application/json" -d '{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2024-01-15T13:00:00Z"}' http://127.0.0.1:8000
```

or use the fake client for randomized requests:

```bash
# linux / macOS
python3 fake_client.py
# Windows
python fake_client.py
```

### How to run tests

The tests are located in the `tests` directory. I used FastAPI's `TestClient` to test the API.
and simple `pytest` compatible functions to create unit tests for all the small parts as well
as more general tests for the entirety of the API.

To run the tests, run the following command in the root directory of the project:

```bash
pytest
```
