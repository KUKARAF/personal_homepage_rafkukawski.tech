# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Copy .env file
COPY .env .

# Install system dependencies for building Python packages
RUN apt-get update && apt-get install -y build-essential gcc

# Install any needed packages specified in requirements.txt
# Also install gunicorn for production server
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Add the application directory to PYTHONPATH
ENV PYTHONPATH=/app

# Run the application using gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "rafatech.wsgi:application"]
