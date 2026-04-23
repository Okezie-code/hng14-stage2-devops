from fastapi import FastAPI
import redis
import uuid
import os


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

    if r:
        r.lpush("job", job_id)
        r.hset(f"job:{job_id}", "status", "completed")
    else:
        fake_db[job_id] = "completed"

    return {"job_id": job_id}


@app.get("/jobs/{job_id}")
def get_job(job_id: str):
    return {
        "job_id": job_id,
        "status": "completed"
    }
