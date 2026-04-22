# --------- BUILD STAGE ---------
FROM python:3.11-alpine AS builder

WORKDIR /app

RUN apk add --no-cache gcc musl-dev libffi-dev

COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# --------- FINAL STAGE ---------
FROM python:3.11-alpine

WORKDIR /app

# create non-root user
RUN adduser -D appuser

COPY --from=builder /install /usr/local
COPY . .

USER appuser

EXPOSE 8000

HEALTHCHECK --interval=10s --timeout=5s --retries=5 CMD wget -qO- http://localhost:8000/jobs || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
