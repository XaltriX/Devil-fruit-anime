# Use Python slim image
FROM python:3.10-slim-buster

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt requirements.txt

# Install Python dependencies
RUN pip3 install --upgrade pip \
    && pip3 install -r requirements.txt

# Copy app code
COPY . .

# Run bot
CMD ["python3", "main.py"]
