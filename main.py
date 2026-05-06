from __future__ import annotations
import json
from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Any, Literal

app = FastAPI()

class Patient(BaseModel):
    id: str = Field(
        default="P001",
        description="Enter Patient ID",
        examples=["P001"]
    )

    name: str = Field(
        default="Maryam Naseem",
        description="Enter Patient's full name",
        examples=["Maryam Naseem"]
    )

    age: int = Field(
        default=22,
        gt=0,
        lt=110,
        description="Enter Patient's age",
        examples=[22]
    )

    gender: Literal["male", "female", "other"] = Field(
        description="Enter Patient's gender",
        examples=["female"]
    )

    height: float = Field(
        gt=0,
        description="Enter Patient's height in meters",
        examples=[1.75]
    )

    weight: float = Field(
        gt=0,
        description="Enter Patient's weight in kgs",
        examples=[68]
    )

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)

    @computed_field
    @property
    def verdict(self) -> str:
        bmi = self.bmi
        if bmi < 18.5:
            return 'Underweight'
        elif 18.5 <= bmi < 25:
            return 'Normal weight'
        elif 25 <= bmi < 30:
            return 'Overweight'
        else:
            return 'Obese'
        
def load_data() -> dict[str, Any]:
    with open("patients.json", "r") as file:
        return json.load(file)

def save_data(data: dict[str, Any]) -> None:
    with open("patients.json", "w") as file:
        json.dump(data, file)

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

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description= 'Sort on the basis of height, weight or bmi'), order: str = Query('asc', description='sort in asc or desc order')):    
    valid_fields = ['height', 'weight', 'bmi']
    
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')

    data = load_data()
    sort_order = True if order == 'desc' else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)
    return {"patients": sorted_data}

@app.post("/create")
def create_patient(patient: Patient):
    data = load_data()
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient with this ID already exists")
    
    data[patient.id] = patient.model_dump(exclude={'id'})

    save_data(data)
    return  JSONResponse(status_code= 201, content={"message": "Patient created successfully", "patient": data[patient.id]})

