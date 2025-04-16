FROM python:3.11-slim

# Install compilers and tools
RUN apt-get update && apt-get install -y \
    default-jdk \
    g++ \
    curl \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean

# Set working directory
WORKDIR /app

# Copy contents from backend/ into container
COPY backend/ .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Run your app
CMD ["python", "main.py"]
