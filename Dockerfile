FROM python:3.10-slim

ENV TZ="America/Los_Angeles"

WORKDIR /app

ADD . /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt
