FROM python:3.11-slim

# Install Java, Node.js, and other dependencies
RUN apt-get update && \
    apt-get install -y default-jdk curl && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean

# Confirm installations (optional for debug)
RUN java -version && node -v && npm -v

# Set working directory
WORKDIR /app

# Copy the entire project
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r backend/requirements.txt

# Move into backend folder for runtime
WORKDIR /app/backend

# Start the Python server
CMD ["python", "main.py"]
