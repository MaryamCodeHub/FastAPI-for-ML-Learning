from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open("patients.json", "r") as file:
        data = json.load(file)
    return data

@app.get("/")
def home():
    return {"message": "Welcome to the home page!"}

@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}

@app.get("/view")
def view_data():
    data = load_data()
    return {"patients": data}