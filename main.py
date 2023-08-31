"""Main function."""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """Hello world app default."""
    return {"Hello": "World"}
