# Use the official Python image from the Docker Hub
FROM python:3.8-slim as builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies and cleanup in one layer
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    gcc && \
    rm -rf /var/lib/apt/lists/*

# Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Final stage
FROM python:3.8-slim

# Create a non-root user
RUN useradd -m -s /bin/bash appuser

# Set environment variables
ENV PYTHONPATH=/app:/app/rafatech \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Copy only necessary files from builder
COPY --from=builder /usr/local/lib/python3.8/site-packages/ /usr/local/lib/python3.8/site-packages/
COPY --from=builder /usr/local/bin/gunicorn /usr/local/bin/gunicorn
COPY . .

# Collect static files and set permissions
RUN python manage.py collectstatic --noinput && \
    mkdir -p /app/staticfiles && \
    chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Make sure static files are accessible
ENV STATIC_ROOT=/app/staticfiles

# Expose port
EXPOSE 8000

# Healthcheck
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health/ || exit 1

# Run gunicorn with production settings
CMD ["gunicorn", \
     "--bind", "0.0.0.0:8000", \
     "--workers", "4", \
     "--worker-class", "gthread", \
     "--threads", "2", \
     "--timeout", "60", \
     "--keep-alive", "5", \
     "--log-level", "warning", \
     "--access-logfile", "-", \
     "--error-logfile", "-", \
     "rafatech.wsgi:application"]
