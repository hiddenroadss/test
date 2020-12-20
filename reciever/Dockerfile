FROM python:3.8-alpine

RUN pip3 install  pika
RUN apk add --update bash
COPY . /app
WORKDIR '/app'

CMD ["./wait-for-it.sh", "rabbit:5672", "--", "python3", "-u", "./reciever.py"]
