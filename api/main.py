from fastapi import FastAPI
import redis
import uuid
import os

app = FastAPI()

try:
    r = redis.Redis(
        host=os.getenv("REDIS_HOST", "redis"),
        port=int(os.getenv("REDIS_PORT", 6379))
    )
    r.ping()
except Exception:
    print("Redis not available, using fallback")
    r = None


@app.post("/jobs")
def create_job():
    job_id = str(uuid.uuid4())

    if r:
        r.lpush("job", job_id)
        r.hset(f"job:{job_id}", "status", "queued")

    return {"job_id": job_id}


@app.get("/jobs/{job_id}")
def get_job(job_id: str):
    job = r.hgetall(f"job:{job_id}")

    if job == {}:
        return {"error": "not found"}

    status = job.get(b"status")

    return {
        "job_id": job_id,
        "status": status.decode() if status else "unknown"
    }
