import tensorflow as tf
import pickle
import numpy as np
from pydantic import BaseModel
from typing import List
import uvicorn
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import os
import json
import time
from dotenv import load_dotenv

from utils import make_req

load_dotenv()

app = FastAPI()

port = os.environ.get("PORT")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

modelBTC = tf.keras.models.load_model('models/BTC-lstm.h5')
modelETH = tf.keras.models.load_model('models/ETH-lstm.h5')
modelADA = tf.keras.models.load_model('models/ADA-lstm.h5')
modelSOL = tf.keras.models.load_model('models/SOL-lstm.h5')
modelMATIC = tf.keras.models.load_model('models/MATIC-lstm.h5')

loaded_scalarBTC = pickle.load(open('scalers/scaler-BTC.pkl', 'rb'))
loaded_scalarETH = pickle.load(open('scalers/scaler-ETH.pkl', 'rb'))
loaded_scalarADA = pickle.load(open('scalers/scaler-ADA.pkl', 'rb'))
loaded_scalarSOL = pickle.load(open('scalers/scaler-SOL.pkl', 'rb'))
loaded_scalarMATIC = pickle.load(open('scalers/scaler-MATIC.pkl', 'rb'))


class predInput(BaseModel):
    baseID: str
    values: List[float]


@app.get('/healthz')
def healthz():
    return "OK"


@app.get('/prices/')
def prices(start: int = Query(None, alias="start"), end: int = Query(None, alias="end"), baseID: str = Query(None, alias="baseID")):
    # end = datetime.date.today()
    # start = end - datetime.timedelta(days=15)
    # end = int(time.mktime(end.timetuple()) * 1000)
    # start = int(time.mktime(start.timetuple()) * 1000)
    response = make_req(start, end, baseID)
    data = json.loads(response.text)
    res = []
    for i in data['data']:
        res.append(float(i['close']))
    return {
        'prices': res
    }


@app.post("/predict/")
async def predict(input: predInput):
    vals = np.array(input.values)
    pred_input_shaped = vals.reshape(-1, 1)
    if input.baseID == 'bitcoin':
        transformed_input = loaded_scalarBTC.transform(pred_input_shaped)
        input_data = transformed_input.reshape(
            1, transformed_input.shape[0], transformed_input.shape[1])
        prediction = modelBTC.predict(input_data)
        prediction = loaded_scalarBTC.inverse_transform(prediction)
    elif input.baseID == 'ethereum':
        transformed_input = loaded_scalarETH.transform(pred_input_shaped)
        input_data = transformed_input.reshape(
            1, transformed_input.shape[0], transformed_input.shape[1])
        prediction = modelETH.predict(input_data)
        prediction = loaded_scalarETH.inverse_transform(prediction)
    elif input.baseID == 'cardano':
        transformed_input = loaded_scalarADA.transform(pred_input_shaped)
        input_data = transformed_input.reshape(
            1, transformed_input.shape[0], transformed_input.shape[1])
        prediction = modelADA.predict(input_data)
        prediction = loaded_scalarADA.inverse_transform(prediction)
    elif input.baseID == 'solana':
        transformed_input = loaded_scalarSOL.transform(pred_input_shaped)
        input_data = transformed_input.reshape(
            1, transformed_input.shape[0], transformed_input.shape[1])
        prediction = modelSOL.predict(input_data)
        prediction = loaded_scalarSOL.inverse_transform(prediction)
    elif input.baseID == 'polygon':
        transformed_input = loaded_scalarMATIC.transform(pred_input_shaped)
        input_data = transformed_input.reshape(
            1, transformed_input.shape[0], transformed_input.shape[1])
        prediction = modelMATIC.predict(input_data)
        prediction = loaded_scalarMATIC.inverse_transform(prediction)
    else:
        return {
            'error': 'Invalid baseID'
        }

    return {
        'prediction': float(prediction)
    }

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=port)
