import os
import requests
import csv
import datetime
import time
import json
from tqdm import tqdm
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get("COIN_CAP_API_KEY")

start_date = datetime.date(2018, 1, 1)
end_date = datetime.date(2021, 11, 1)
delta = datetime.timedelta(days=1)
range = end_date - start_date
count = range.days + 1

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r


def make_req(start, end):
    url = "http://api.coincap.io/v2/candles?exchange=binance&interval=d1&baseId=bitcoin&quoteId=tether&start={}&end={}".format(
        start, end)

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload, auth=BearerAuth(token))

    return response


with open('data.csv', 'a') as csvfile:
    fieldnames = ['open', 'high', 'low', 'close', 'volume', 'period']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    pbar = tqdm(total = count)
    while start_date <= end_date:
        start = int(time.mktime(start_date.timetuple()) * 1000)
        start_date += delta
        end = int(time.mktime(start_date.timetuple()) * 1000)

        response = make_req(start, end)
        data = json.loads(response.text)
        if len(data['data']) > 0:
            for i in data['data']:
                writer.writerow(i)
            pbar.update(1)
        else:
            pbar.update(1)
            print("No data for this date")
            continue

    pbar.close()