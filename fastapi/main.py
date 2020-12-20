from typing import Optional, Dict

from fastapi import FastAPI
from pydantic import BaseModel
import pika


app = FastAPI()


class Params(BaseModel):
    name: str = None
    value: str = None


class Item(BaseModel):
    task_id: str
    title: str
    params: Optional[Params] = None


def rabbit_send(new_task):
    parameters = pika.ConnectionParameters('rabbit', 5672)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue='some_queue')

    channel.basic_publish(exchange='', routing_key='some_queue', body=new_task)
    connection.close()


@app.post('/add_task')
def add_task(item: Item):
    rabbit_send(item.json())
