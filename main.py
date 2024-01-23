from fastapi import FastAPI
import random

app = FastAPI()


@app.get("/")
def read_root():
    return {"Testing": "Something", "number": random.randint(1, 100)}
