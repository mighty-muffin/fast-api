# fast-api

## Project

## Code

## Container

Build the container locally

```bash
export FEATURE_GOODBYE="True"
export FEATURE_HEALTH="True"

docker build --secret id=FEATURE_GOODBYE \
             --secret id=FEATURE_HEALTH \
             --target=production \
             --no-cache \
             -f docker/Dockerfile . -t fast-api_local
```

Run container locally for testing purpose

```bash
docker run -p 8080:8080 fast-api_local
```

## Infrastructure
