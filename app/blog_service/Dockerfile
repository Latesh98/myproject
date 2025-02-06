# Blog Service Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY blog_service.py /app/
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "blog_service.py"]
