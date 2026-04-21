# Stage 1: Build
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Final
FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /usr/local /usr/local
COPY . .

# Create non-root user
RUN useradd -m appuser
USER appuser

# Healthcheck
HEALTHCHECK CMD pgrep -f worker.py || exit 1

CMD ["python", "worker.py"]
