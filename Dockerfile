FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libffi-dev \
    && pip install --no-cache-dir uv \
    && apt-get remove -y gcc libffi-dev \
    && apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

RUN uv venv
RUN uv run pip install . --no-cache-dir

ENTRYPOINT ["uv", "run", "sanic", "server"]
