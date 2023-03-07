FROM python:3.9-slim-buster as build

WORKDIR /opt/Scanner

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        libffi-dev \
        libssl-dev \
        git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY . /opt/Scanner

FROM python:3.9-slim-buster as release
WORKDIR /opt/Scanner


RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libffi6 \
        libssl1.1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY --chown=1001:1001 . /opt/Scanner


