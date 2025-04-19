FROM python:3.11-slim

# Install Java, Node.js, g++, and other dependencies
RUN apt-get update && \
    apt-get install -y default-jdk curl g++ && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean

# Confirm installations (optional debugging)
RUN java -version && node -v && g++ --version

# Set working directory
WORKDIR /app

# Copy your entire app
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r backend/requirements.txt

# Set working directory to backend to run the server
WORKDIR /app/backend

# Run the backend server
CMD ["python", "main.py"]
