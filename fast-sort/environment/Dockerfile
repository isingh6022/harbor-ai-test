FROM python:3.12-slim

# curl is used by tests/test.sh to install uv for the verifier.
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
