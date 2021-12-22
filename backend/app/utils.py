import requests
import os
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get("COIN_CAP_API_KEY")


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r


def make_req(start, end, baseID):
    url = "http://api.coincap.io/v2/candles?exchange=binance&interval=d1&baseId={}&quoteId=tether&start={}&end={}".format(
        baseID, start, end)

    payload = {}
    headers = {}

    response = requests.request(
        "GET", url, headers=headers, data=payload, auth=BearerAuth(token))

    return response
