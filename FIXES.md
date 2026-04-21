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
Updated the worker to read Redis host and port from environment variables (REDIS_HOST, REDIS_PORT).





Issue 3: Missing Retry Logic in Worker
File: worker/worker.py
Problem:
The worker attempted to connect to Redis immediately on startup and failed if Redis was not yet ready.
Fix:
Implemented retry logic to repeatedly attempt connection until Redis becomes available.





Issue 4: Hardcoded API URL in Frontend
File: frontend/app.js
Problem:
The frontend used a hardcoded API URL, making it incompatible with different environments (e.g., Docker, production).
Fix:
Replaced the hardcoded API URL with an environment variable (API_URL).





Issue 5: Missing Environment Variable Support
File: Multiple files
Problem:
Application configuration values were hardcoded instead of being environment-driven, violating best practices for containerized applications.
Fix:
Introduced environment variables and ensured all services read configuration dynamically.




Issue 6: Services Not Container-Ready
File: Entire project
Problem:
The application was not designed to run in containers due to assumptions about localhost networking and startup order.
Fix:
Refactored configuration and service communication to work within Docker networks using service names.
