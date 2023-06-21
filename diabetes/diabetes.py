from pydantic import BaseModel

class Diabetes(BaseModel):
    gender: int
    age: int
    hypertension: int
    heart_disease: int 
    bmi: int
    HbA1c_level: int
    blood_glucose_level: int