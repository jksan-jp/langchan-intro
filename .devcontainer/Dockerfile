FROM python:3.11-slim-buster

WORKDIR /workspace

COPY .devcontainer/requirements.txt /workspace

RUN pip install --upgrade pip && pip install -r requirements.txt
