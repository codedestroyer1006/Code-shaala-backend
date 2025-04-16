FROM python:3.11-slim

# Install Java, g++, Node.js (for code execution)
RUN apt-get update && apt-get install -y \
    default-jdk \
    g++ \
    curl \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean

# Set the correct working directory
WORKDIR /app

# Copy everything into the container's /app directory
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your app runs on
EXPOSE 5000

# Run your backend script
CMD ["python", "main.py"]
