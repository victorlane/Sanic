FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install uv

WORKDIR /app
COPY . /app

RUN uv venv
RUN uv run pip install .

ENTRYPOINT ["uv", "run", "sanic", "server"]
