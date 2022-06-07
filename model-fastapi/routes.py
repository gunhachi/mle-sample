import numpy as np
from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse

from models import PredictRequest, PredictResponse
from inference import Model, get_model

api = APIRouter()

@api.get("/app")
def read_index():
    return FileResponse("./app.html")

@api.post("/predict", response_model=PredictResponse)
def predict(input: PredictRequest, model: Model = Depends(get_model)):
    data = []
    for _,v in input:
        data.append(v)
    X = np.array([data])
    y_pred = model.predict(X)
    result = PredictResponse(data=y_pred)
    return result
