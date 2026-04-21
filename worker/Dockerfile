FROM python:3.11-slim

WORKDIR /app

# Install curl (optional but safe)
RUN apt-get update && apt-get install -y curl

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Create non-root user
RUN useradd -m appuser
USER appuser

# Healthcheck (check if process is running)
HEALTHCHECK CMD pgrep -f worker.py || exit 1

# Start worker
CMD ["python", "worker.py"]
