import os
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

app = FastAPI()

FEATURE_GOODBYE = os.getenv("FEATURE_GOODBYE")
FEATURE_HEALTH = os.getenv("FEATURE_HEALTH")


@app.get("/")
def hello(name: str = "World"):
    return f"Hello, {name}!"


if FEATURE_GOODBYE:

    @app.get("/goodbye")
    def goodbye(name: str = "World"):
        return f"Goodbye, {name}!"


if FEATURE_HEALTH:

    @app.get("/healthcheck")
    def healthcheck():
        return {"status": "healthy"}
