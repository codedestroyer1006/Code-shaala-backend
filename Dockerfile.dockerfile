# Use official Python image
FROM python:3.11-slim

# Install compilers
RUN apt-get update && apt-get install -y \
    default-jdk \
    g++ \
    nodejs \
    npm \
    && apt-get clean

# Set working directory
WORKDIR /app

# Copy everything into container
COPY backend/ .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Start the Flask server
CMD ["python", "main.py"]
