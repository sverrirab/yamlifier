FROM python:2.7-slim

WORKDIR /code
ADD / /code
RUN pip install -e .
