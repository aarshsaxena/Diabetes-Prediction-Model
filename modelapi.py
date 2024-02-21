from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app=FastAPI()

# load model 
diabetes_model=pickle.load(open('classifier.sav','rb'))

class model_input(BaseModel):

    # input features
    gender: int
    age: float
    hypertension: int 
    heart_disease: int
    bmi: float 
    HbA1c_level: float
    blood_glucose_level: int




@app.post( '/diabetes_prediction' )
def model_prediction( input_parameters: model_input) :
    input_data = input_parameters.json() #data to json format
    input_dictionary=json.loads(input_data) #json data  to dictionary

    input_list=[input_dictionary['gender'],input_dictionary['age'],input_dictionary['hypertension'],input_dictionary['heart_disease'],input_dictionary['bmi'],input_dictionary['HbA1c_level'],input_dictionary['blood_glucose_level']]

    prediction=diabetes_model.predict([input_list])

    if (prediction[0]==0):
        return "Person is not diabetic"
    else:
        return "Person is diabetic"
