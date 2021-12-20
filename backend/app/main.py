import tensorflow as tf
import pickle
import numpy as np
from pydantic import BaseModel
from typing import List
import uvicorn
from fastapi import FastAPI

app = FastAPI()

model = tf.keras.models.load_model('models/BTC-lstm.h5')

loaded_scalar = pickle.load(open('scalers/scaler-BTC.pkl', 'rb'))

class Input(BaseModel):
    values: List[float]

@app.get('/')
def index():
    return {"Hello": "World"}

@app.post("/predict")
async def predict(input: Input):
    vals = np.array(input.values)
    pred_input_shaped = vals.reshape(-1, 1)
    transformed_input = loaded_scalar.transform(pred_input_shaped)
    input_data = transformed_input.reshape(
        1, transformed_input.shape[0], transformed_input.shape[1])
    mdlprediction = model.predict(input_data)
    prediction = loaded_scalar.inverse_transform(mdlprediction)
    return {
        'prediction': float(prediction)
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
