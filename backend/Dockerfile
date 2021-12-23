FROM python:3.8-slim

COPY . /project

WORKDIR /project

RUN apt-get update && apt-get install -y python3-pip

ENV COIN_CAP_API_KEY=${COIN_CAP_API_KEY}

ENV PORT=${PORT}

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD [ "python3", "app/main.py" ]

