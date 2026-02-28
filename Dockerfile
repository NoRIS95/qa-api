FROM python:3.12-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH=/app

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    make \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install uv

WORKDIR /app

COPY uv.lock pyproject.toml ./
COPY app/alembic.ini ./
RUN uv venv && uv sync

COPY app/ ./app/
ENV PATH="/app/.venv/bin:$PATH"
EXPOSE 8000
RUN which uvicorn || echo "uvicorn not found in PATH"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]