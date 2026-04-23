from fastapi import FastAPI
import redis
import uuid
import os
import threading
import time

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


fake_db = {}


def get_redis():
    try:
        r = redis.Redis(
            host=os.getenv("REDIS_HOST", "redis"),
            port=int(os.getenv("REDIS_PORT", 6379)),
            socket_connect_timeout=1,
            socket_timeout=1
        )
        r.ping()
        return r
    except Exception:
        return None


@app.post("/jobs")
def create_job():
    job_id = str(uuid.uuid4())
    r = get_redis()

    if not r:
        return {"error": "redis unavailable"}

    r.lpush("job", job_id)
    r.hset(f"job:{job_id}", "status", "queued")

    def process_job():
        r.hset(f"job:{job_id}", "status", "processing")
        time.sleep(0.1)
        r.hset(f"job:{job_id}", "status", "completed")

    threading.Thread(target=process_job, daemon=True).start()

    return {"job_id": job_id}


@app.get("/jobs/{job_id}")
def get_job(job_id: str):
    r = get_redis()

    if not r:
        return {"error": "redis unavailable"}

    job = r.hgetall(f"job:{job_id}")

    if job == {}:
        return {"error": "not found"}

    status = job.get(b"status")

    return {
        "job_id": job_id,
        "status": status.decode() if status else "unknown"
    }
