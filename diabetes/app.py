#importing libraries
import uvicorn
from fastapi import FastAPI
from diabetes import Diabetes
import numpy as np
import pickle
import pandas as pd

app=FastAPI()
pickle_in=open("classifier.pkl","rb")
knn=pickle.load(pickle_in)

@app.get('/')
def index():
    return {'message': 'Hello World'}

@app.post('/predict')
def pridiction_diabetes(data1:Diabetes):
    gender: data1['gender']
    age: data1['age']
    hypertension: data1['hypertension']
    heart_disease: data1['heart_disease']
    bmi: data1['bmi']
    HbA1c_level: data1['HbA1c_level']
    blood_glucose_level: data1['blood_glucose_level']
    ans=knn.predict([[gender,age,hypertension,heart_disease,bmi,HbA1c_level,blood_glucose_level]])

    if ans[0]==1:
        ans="Diabetes is Presence"
    else:
        ans="Diabetes is absent"

    return {'ans': ans}


#Run the API with uvicorn
if __name__=='__main__':
    uvicorn.run(app)
    
    # uvicorn app name: app --reload                #to run the uvicorn