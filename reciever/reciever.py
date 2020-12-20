import pika


def callback(ch, method, properties, body):
    print(body)


def receive_message():
    parameters = pika.ConnectionParameters('rabbit', 5672)
    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()

    channel.queue_declare(queue='some_queue')

    channel.basic_consume(queue='some_queue', on_message_callback=callback)

    print('Waiting for messages')
    channel.start_consuming()


receive_message()
