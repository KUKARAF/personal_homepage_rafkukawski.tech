# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
# Also install gunicorn for production server
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the application using gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
