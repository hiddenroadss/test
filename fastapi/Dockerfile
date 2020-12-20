FROM python:3.8-alpine

RUN pip3 install fastapi uvicorn pika
COPY . /app
WORKDIR '/app'

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8500"]

