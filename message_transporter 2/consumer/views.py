import json
import pika
from database import DatabaseHandler  # Assuming you have a DatabaseHandler class for database interactions


def callback(ch, method, properties, body):
    data = json.loads(body)
    db_handler = DatabaseHandler()
    for i in range(len(data)):
        
        # Sanitize data and write to the database
        db_handler.save_product_data(
            data[i].get('meta_info',''), 
            data[i].get('available_price',''),    
            data[i].get('stock',''),  
            data[i].get('source','')    
        )


# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue
channel.queue_declare(queue='data_queue')

# Set up a callback function
channel.basic_consume(queue='data_queue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
