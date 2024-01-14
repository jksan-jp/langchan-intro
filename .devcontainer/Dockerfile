FROM python:3.11-slim-buster
USER root

RUN apt-get update  && \
    apt-get install -y make

WORKDIR /workspace
COPY .devcontainer/requirements.txt /workspace
RUN pip install --upgrade pip && pip install -r requirements.txt
