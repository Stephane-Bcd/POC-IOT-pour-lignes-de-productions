import pika
import time


'''
    Function to get a message and print it in console
'''
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")


'''
    Connecting to Rabbitmq
'''
credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')
parameters = pika.ConnectionParameters('localhost',
                                       5672,
                                       'Client1',
                                       credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

'''
post a message from a client
'''

channel.basic_publish(exchange='Client1-Maison1',
                      routing_key='',
                      body='Hello World!')


'''
    Get message from client1 queue
'''

channel.basic_consume(queue='Client1',
                      on_message_callback=callback,
                      auto_ack=True
                    )

'''
    Disconnecting from Rabbitmq
'''
connection.close()
