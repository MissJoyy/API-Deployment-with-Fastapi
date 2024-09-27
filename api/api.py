from fastapi import FastAPI
import joblib
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

class SepsisFeatures(BaseModel):
    PRG: int
    PL: int
    PR: int
    SK: int
    TS: int
    M11: float
    BD2: float
    Age: int
    Insurance: int

@app.get('/')
def status_check():
    return {'status': 'API is Online...'}

@app.get('/documents')
def documentation():
    return {'All documentation': 'API Documentation...'}

forest_pipeline = joblib.load('./models/forest_pipeline.joblib') 
encoder = joblib.load('./models/encoder.joblib') 

@app.post('/forest_prediction')
def predict_Sepsiss_Status(data: SepsisFeatures):
    try:
        df =  pd.DataFrame([data.model_dump()])
        prediction = forest_pipeline.predict(df)
        encoded_prediction = prediction[0]
        prediction_probability = forest_pipeline.predict_proba(df)[0].tolist()
        response ={
            'prediction': encoded_prediction,
            'probababilties':{'Negative':round(prediction_probability[0],2),
                             'Positive':round(prediction_probability[1],2)} 
        }
        return response
    except Exception as e:
        return {"error":str(e)}



app.get('/')
def status_check():
    return {'status': 'API is Online...'}

@app.get('/documents')
def documentation():
    return {'All documentation': 'API Documentation...'}

knc_pipeline = joblib.load('./models/knc_pipeline.joblib') 
encoder = joblib.load('./models/encoder.joblib') 

@app.post('/knc_prediction')
def predict_Sepsiss_Status(data: SepsisFeatures):
    try:
        df =  pd.DataFrame([data.model_dump()])
        prediction = knc_pipeline.predict(df)
        encoded_prediction = prediction[0]
        prediction_probability = knc_pipeline.predict_proba(df)[0].tolist()
        response ={
            'prediction': encoded_prediction,
            'probababilties':{'Negative':round(prediction_probability[0],2),
                             'Positive':round(prediction_probability[1],2)} 
        }
        return response
    except Exception as e:
        return {"error":str(e)}



      