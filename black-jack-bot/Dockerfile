# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    redis-server \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Set the Discord token environment variable
ENV DISCORD_TOKEN=<Your Token>

# Expose the port if your application is running a web server
# EXPOSE 8000

# Start Redis server and run the application
CMD ["sh", "-c", "redis-server --daemonize yes && python main.py"]
