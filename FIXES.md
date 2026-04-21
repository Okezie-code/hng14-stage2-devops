Issue 1: Hardcoded Redis Host in API
File: api/main.py
Line: (specify actual line if you remember, else approximate)
Problem:
The Redis host was hardcoded, which prevents the application from working in a containerized environment where services communicate via Docker network names.
Fix:
Replaced the hardcoded Redis host with an environment variable (REDIS_HOST) to allow dynamic configuration.





Issue 2: Hardcoded Redis Host in Worker
File: worker/worker.py
Problem:
The worker service used a hardcoded Redis host, causing failure when running inside Docker containers.
Fix:
Updated the worker to read Redis host and port from environment variables (REDIS_HOST, REDIS_PORTIssue 1: Hardcoded Redis Host in API
File: api/main.py
Line: 8–11
Problem:
The Redis connection in the API used a default fallback to "localhost", which breaks in a containerized environment where services must communicate via Docker service names.
Fix:
Replaced the hardcoded fallback with environment variable usage (REDIS_HOST, REDIS_PORT) to allow proper service discovery within Docker.





Issue 2: Hardcoded Redis Host in Worker
File: worker/worker.py
Line: 6–9
Problem:
The worker service depended on "localhost" as the Redis host fallback, which fails when running inside containers.
Fix:
Updated the Redis connection to use environment variables (REDIS_HOST, REDIS_PORT) for correct inter-container communication.





Issue 3: Missing Retry Logic for Redis Connection
File: worker/worker.py
Line: 18–25
Problem:
The worker attempted to connect to Redis immediately on startup. If Redis was not yet ready, the worker would fail.
Fix:
Implemented retry logic using a loop with exception handling (redis.exceptions.ConnectionError) and delay (time.sleep) to wait until Redis becomes available.





Issue 4: Hardcoded API URL in Frontend
File: frontend/app.js
Line: 6
Problem:
The frontend used a hardcoded API URL (http://localhost:8000), making it inflexible and incompatible with containerized deployments.
Fix:
Replaced the hardcoded API URL with an environment variable (API_URL) with a fallback, allowing dynamic configuration across environments.





Issue 5: Configuration Not Environment-Driven
File: Multiple files (api/main.py, worker/worker.py, frontend/app.js)
Problem:
Key configuration values (Redis host, API URL) were hardcoded, violating best practices for containerized applications.
Fix:
Refactored all services to use environment variables for configuration, ensuring portability and flexibility across environments.





Issue 6: Application Not Container-Ready
File: Entire project
Problem:
The application assumed localhost-based communication and lacked proper service discovery, causing failures inside Docker.
Fix:
Updated all services to communicate using Docker service names and environment variables, making the system fully container-compatible.
