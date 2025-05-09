from fastapi import FastAPI

app = FastAPI()

FEATURE_GOODBYE = True
FEATURE_HEALTH = True


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
