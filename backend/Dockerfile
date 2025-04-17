# Use a base image with Python and Java
FROM python:3.11-slim

# Install Java
RUN apt-get update && apt-get install -y default-jdk

# Set the working directory
WORKDIR /app

# Copy your backend code into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (adjust if needed)
EXPOSE 8000

# Command to run your app
CMD ["python", "main.py"]
