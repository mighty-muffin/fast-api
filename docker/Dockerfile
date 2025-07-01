## ------------------------------- Builder Stage ------------------------------ ##
FROM python:3.13-bookworm@sha256:be97a205ac2f0d0662cc312d5cfeb835129f23dd9bc9559e02d686656af1bd52 AS builder

RUN apt-get update && apt-get install --no-install-recommends -y \
        build-essential curl &&\
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Download the latest installer, install it and then remove it
ADD https://astral.sh/uv/install.sh /install.sh
RUN chmod -R 755 /install.sh && /install.sh && rm /install.sh

# Set up the UV environment path correctly
ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /app

COPY fast-api/pyproject.toml .

RUN uv sync

## ------------------------------- Production Stage ------------------------------ ##
FROM python:3.13-slim-bookworm@sha256:6544e0e002b40ae0f59bc3618b07c1e48064c4faed3a15ae2fbd2e8f663e8283 AS production

RUN useradd --create-home appuser
USER appuser

WORKDIR /app

COPY /fast-api/src src
COPY --from=builder /app/.venv .venv

# Set up environment variables for production
ENV PATH="/app/.venv/bin:$PATH"

# Expose the specified port for FastAPI
EXPOSE $PORT

# Start the application with Uvicorn in production mode, using environment variable references
CMD ["uvicorn", "src.main:app", "--log-level", "info", "--host", "0.0.0.0" , "--port", "8080"]
