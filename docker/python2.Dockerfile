FROM python:2.7-slim

WORKDIR /build
ADD requirements.txt /build

RUN pip install -r requirements.txt

WORKDIR /code
ADD / /code
RUN pip install -e .
