from fastapi import FastAPI, Path, HTTPException
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

@app.get("/patients/{patient_id}")
def get_patient(patient_id: str = Path(..., description="The ID of the patient in the DB", example="P001")):

    data = load_data()

    if patient_id in data:
        return {"patient": data[patient_id]}
    raise HTTPException(status_code=404, detail="Patient not found")