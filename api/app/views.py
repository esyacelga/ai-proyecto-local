from .model import PredictionRequest
from .utils import get_model, transform_to_dataframe




def get_prediction(request: PredictionRequest, path: str) -> float:
    model = get_model(path)
    data_to_predict = transform_to_dataframe(request)
    prediction = model.predict(data_to_predict)[0]
    return max(0, prediction)


def saludar(nombre):
    return f"Hola, {nombre}!"
