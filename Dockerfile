FROM python:3.11-buster

ENV PYTHONBUFERED=1

WORKDIR /frontend

RUN apt-get update && apt-get install -y --no-install-recommends \
	curl \
	vim \
	&& rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && \
	pip install poetry

COPY pyproject.toml* poetry.lock* ./

RUN poetry config virtualenvs.in-project true
RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi