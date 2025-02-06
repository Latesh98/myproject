# User Service Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY user_service.py /app/
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "user_service.py"]
