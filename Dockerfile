# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY website.py website.py

COPY run.sh run.sh

CMD [ "/app/run.sh","8001" ] 
