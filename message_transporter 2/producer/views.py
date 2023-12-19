# Create your views here.
import json
import pika


def produce_to_queue(file_path, queue_name):
    # Connect to RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare a queue
    channel.queue_declare(queue=queue_name)

    # Read data from the file
    with open(file_path, 'r') as file:
        newdata = file.read()
        data = json.loads(newdata)
        
    # Send data to the queue
    channel.basic_publish(exchange='', routing_key=queue_name, body=json.dumps(data))

    print(" [x] Sent data to the queue")

    # Close connection
    connection.close()


# Usage
produce_to_queue('/Users/user/Downloads/assignment_updated.json', 'data_queue')