from fastapi import FastAPI
from regresion_lineal_simple.src.notebooks.classes import salary_model 
from .app.views import get_prediction



app = FastAPI(docs_url='/')


@app.post('/v1/salaryPrediction')
def salary_prediction_model_prediction(request: salary_model.SalaryPredictionRequest):
    return salary_model.SalaryPredictionResponse(Salary=get_prediction(request,'regresion_lineal_simple/src/notebooks/model/model.pkl'))
