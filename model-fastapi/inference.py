from models import PredictRequest, PredictResponse
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
import joblib
import numpy as np

class Model:
    def __init__(self, model_path: str = None):
        self._model = None
        self._model_path = model_path
        self.load()

    def train(self, X: np.ndarray, y: np.ndarray):
        self._model = LinearRegression()
        self._model.fit(X, y)
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        return self._model.predict(X)

    def save(self):
        if self._model is not None:
            joblib.dump(self._model, self._model_path)
        else:
            raise TypeError("The model is not trained yet, use .train() before saving")

    def load(self):
        try:
            self._model = joblib.load(self._model_path)
        except:
            self._model = None
        return self

model_path = "./weight/model.joblib"
model = Model(model_path)

def get_model():
    return model

