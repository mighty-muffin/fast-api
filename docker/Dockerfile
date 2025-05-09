## ------------------------------- Builder Stage ------------------------------ ##
FROM python:3.12-bookworm@sha256:564adc572923a83959dce17dc293d521b3329e930b3e5b8aa98bc50b3d25f8d1 AS builder

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
FROM python:3.12-slim-bookworm@sha256:bae1a061b657f403aaacb1069a7f67d91f7ef5725ab17ca36abc5f1b2797ff92 AS production

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
