
FROM python:alpine

# Install Java, g++, Node.js
RUN apt-get update && apt-get install -y \
    default-jdk \
    g++ \
    curl \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean

# Set working directory
WORKDIR /app

# Copy everything into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (Flask or FastAPI)
EXPOSE 5000

# Run your app
CMD ["python", "main.py"]