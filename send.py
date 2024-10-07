import pika

def main():
    # Set up the connection and channel
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # Declare a queue named 'hello'
    channel.queue_declare(queue='hello')

    # The message to send
    message = 'Hello, World!'
    
    # Send the message to the queue
    channel.basic_publish(exchange='', routing_key='hello', body=message)
    print(f" [x] Sent '{message}'")

    # Close the connection
    connection.close()

if __name__ == '__main__':
    main()
