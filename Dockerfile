# Use the official Python image from the Docker Hub
FROM python:3.10-slim

RUN apt update -y && apt install awscli -y

# Set the working directory
WORKDIR /app

# Install build tools and HDF5 dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    pkg-config \
    libhdf5-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN python -m pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files to the working directory
COPY . .

# Expose the port that the app runs on
EXPOSE 8080

# Command to run the application
CMD ["python", "app.py"]
