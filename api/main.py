from fastapi import FastAPI
from .app.views import get_prediction
from .app.regresion_lineal_simple import salary_model 
from .app.classes.regresion_lineal_multiple import profit_classes
from .app.classes.regresion_lineal_polinomica import ice_cream_classes
 
 



app = FastAPI(docs_url='/')


@app.post('/v1/salaryPrediction')
def salary_prediction_model_prediction(request: salary_model.SalaryPredictionRequest):
    return salary_model.SalaryPredictionResponse(Salary=get_prediction(request,'regresion_lineal_simple/src/notebooks/model/model-salary.pkl'))


@app.post('/v1/profitPrediction')
def profit_prediction_model_prediction(request: profit_classes.ProfitRequest):
    return profit_classes.ProfitResponse(Profit=get_prediction(request,'regresion_lineal_multiple/src/notebooks/model/model-profit.pkl'))

@app.post('/v1/iceCreamPrediction')
def ice_cream_prediction_model_prediction(request: ice_cream_classes.IceCreamRequest):
    return ice_cream_classes.IceCreamResponse(units_ice_cream=get_prediction(request,'regresion-lineal-polinomica/src/notebooks/model/model-polinomic.pkl'))
