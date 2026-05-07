from __future__ import annotations
import json
from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Any, Literal, Optional, Annotated

app = FastAPI()

#Pydantic BaseModel
class Patient(BaseModel):
    id: str = Field(
        ...,
        description="Enter Patient ID",
        examples=["P001"]
    )

    name: str = Field(
        ...,
        description="Enter Patient's full name",
        examples=["Maryam Naseem"]
    )

    age: int = Field(
        ...,
        gt=0,
        lt=110,
        description="Enter Patient's age",
        examples=[22]
    )

    gender: Literal["male", "female", "other"] = Field(
        ...,
        description="Enter Patient's gender",
        examples=["female"]
    )

    height: float = Field(
        ...,
        gt=0,
        description="Enter Patient's height in meters",
        examples=[1.75]
    )

    weight: float = Field(
        ...,
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

#creating pydantic basemodel for updating patient info
class PatientUpdate (BaseModel):
    name: Annotated [Optional [str], Field(default=None)]
    city: Annotated [Optional [str], Field(default=None)]
    age: Annotated [Optional [int], Field(default=None, gt=0)]
    gender: Annotated [Optional [Literal['male', 'female']], Field(default=None)]
    height: Annotated [Optional [float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]


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

#RETREIVE API endpoint:
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

#CREATE API endpoint:
@app.post("/create")
def create_patient(patient: Patient):
    data = load_data()
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient with this ID already exists")
    
    data[patient.id] = patient.model_dump(exclude={'id'})

    save_data(data)
    return  JSONResponse(status_code= 201, content={"message": "Patient created successfully", "patient": data[patient.id]})


@app.put('/edit/{patient_id}')
def update_patient(patient_id: str, patient_update: PatientUpdate):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=484, detail='Patient not found')
    
    existing_patient_info = data[patient_id]
    updated_patient_info = patient_update.model_dump(exclude_unset=True)

    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value

    
    #existing patient_info -> pydantic object -> updated bmi verdict
    existing_patient_info['id'] = patient_id
    patient_pydandic_obj = Patient(**existing_patient_info)

    #-> pydantic object -> dict
    existing_patient_info = patient_pydandic_obj.model_dump(exclude={'id'})
    
    #add this dict to data
    data [patient_id] = existing_patient_info
    
    #save data
    save_data(data)

    return JSONResponse(status_code=200, content={"message": "Patient updated successfully", "patient": data[patient_id]})


#DELETE API endpoint:
@app.delete("/delete/{patient_id}")
def delete_patient(patient_id: str):
    
    #loading data
    data =  load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")

    del data[patient_id]
    save_data(data)
    return JSONResponse(status_code=200, content={"message": "Patient deleted successfully"})