FROM python:3.12-slim
WORKDIR /app
COPY app.py .

# Install curl for healthcheck
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Healthcheck
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080 || exit 1

# Run unbuffered Python app
CMD ["python", "-u", "app.py"]
