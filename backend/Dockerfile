# ✅ Base image with Python 3.11
FROM python:3.11

# ✅ Install Java (for 'javac') and other compilers
RUN apt-get update && apt-get install -y \
    default-jdk \
    g++ \
    nodejs \
    npm \
    && apt-get clean

# ✅ Optional: install Node.js if JS runner uses it
RUN npm install -g node

# ✅ Set working directory inside container
WORKDIR /app

# ✅ Copy all backend files into the image
COPY . .

# ✅ Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Expose the port your app runs on (usually 5000 for Flask/FastAPI)
EXPOSE 5000

# ✅ Run your backend app
CMD ["python", "main.py"]
