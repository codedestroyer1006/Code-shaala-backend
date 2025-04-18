FROM python:3.11-slim

# Install Java
RUN apt-get update && apt-get install -y default-jdk

# Set working dir
WORKDIR /app

# Copy files
COPY . .

# Install Python dependencies
RUN pip install -r requirements.txt

# Start the server
CMD ["python", "main.py"]
