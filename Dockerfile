FROM python:3.12-slim AS builder

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# Set the working directory
WORKDIR /myapp

# Copy and install dependencies separately for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Use a lightweight runtime stage
FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Set the working directory
WORKDIR /myapp

# Copy only the installed dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application source code
COPY . .

# Ensure a non-root user runs the container
RUN useradd -m appuser && chown -R appuser /myapp
USER appuser

# Expose port
EXPOSE 8000

# Command to run the application
CMD ["gunicorn", "app.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
