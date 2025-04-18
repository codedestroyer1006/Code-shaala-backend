FROM python:3.11-slim

# Install Java
RUN apt-get update && \
    apt-get install -y default-jdk && \
    apt-get clean

# Set workdir
WORKDIR /app

# Copy and install requirements
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY backend/ .

# Expose port and run
EXPOSE 8000
CMD ["python", "main.py"]
