from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the home page!"}

@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}
