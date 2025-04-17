FROM python:3.11

RUN apt-get update && apt-get install -y default-jdk

WORKDIR /app

COPY backend/ ./backend/

WORKDIR /app/backend

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]
