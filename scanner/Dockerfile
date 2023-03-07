FROM python:3.9-slim-buster as build

WORKDIR /opt/scanner

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

COPY --chown=1001:1001 . /opt/scanner

RUN pip install --no-cache-dir -r requirements.txt


