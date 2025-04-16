# Use Python as base image
FROM python:3.11-slim

# Install required packages
RUN apt-get update && apt-get install -y \
    default-jdk \
    g++ \
    curl \
    && apt-get clean

# Set working directory
WORKDIR /app

# Copy code
COPY backend/ .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Start Flask app
CMD ["python", "main.py"]
