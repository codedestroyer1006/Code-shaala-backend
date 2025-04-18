FROM python:3.11-slim

# Install Java
RUN apt-get update && apt-get install -y default-jdk

# Set working directory
WORKDIR /app

# Copy all project files
COPY . .

# Install Python dependencies
RUN pip install -r backend/requirements.txt

# Run your app
CMD ["python", "backend/main.py"]
