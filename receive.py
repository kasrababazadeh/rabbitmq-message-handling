import pika

def callback(ch, method, properties, body):
    print(f" [x] Received '{body.decode()}'")

def main():
    # Set up the connection and channel
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # Declare a queue named 'hello'
    channel.queue_declare(queue='hello')

    # Tell RabbitMQ that this callback function should receive messages from the 'hello' queue
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    main()
