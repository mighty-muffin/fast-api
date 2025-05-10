## ------------------------------- Builder Stage ------------------------------ ##
FROM python:3.13-bookworm@sha256:ee8747fc77699389c19486f15346466285731b4cb1378c514be1da9dbd399fba AS builder

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
FROM python:3.13-slim-bookworm@sha256:914bf5c12ea40a97a78b2bff97fbdb766cc36ec903bfb4358faf2b74d73b555b AS production

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
