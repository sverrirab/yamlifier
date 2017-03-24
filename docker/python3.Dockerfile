FROM python:3.5-slim

WORKDIR /code
ADD / /code
RUN pip install -e .
