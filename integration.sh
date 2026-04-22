#!/bin/bash

set -e

echo "Waiting for API..."
sleep 5

echo "Creating job..."
JOB_ID=$(curl -s -X POST http://localhost:8000/jobs | jq -r '.job_id')

echo "Fetching job..."
curl -s http://localhost:8000/jobs/$JOB_ID

echo "Integration test complete"
