FROM python:3.11-slim

# Install Java
RUN apt-get update && apt-get install -y default-jdk

# Set working directory
WORKDIR /app

# Copy the entire repo (including backend folder)
COPY . .

# Install dependencies from the correct path
RUN pip install -r backend/requirements.txt

# Set working dir to backend to run the app
WORKDIR /app/backend

# Run the backend server
CMD ["python", "main.py"]
