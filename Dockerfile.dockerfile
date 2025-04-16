FROM python:3.11-slim

# Install required system packages
RUN apt-get update && \
    apt-get install -y openjdk-17-jdk gcc g++ curl && \
    apt-get clean

# Set working directory
WORKDIR /app

# Copy all backend files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 5000

# Run the app
CMD ["python", "main.py"]
