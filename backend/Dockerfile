FROM python:3.11-slim

# Install required tools: Java (javac), g++, node, npm
RUN apt-get update && apt-get install -y \
    default-jdk \
    g++ \
    curl \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (adjust if needed)
EXPOSE 5000

# Start the backend (change this if you're using FastAPI or something else)
CMD ["python", "main.py"]
