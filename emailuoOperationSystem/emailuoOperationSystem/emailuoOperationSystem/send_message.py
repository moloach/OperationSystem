import pika

credential = pika.PlainCredentials('moloach', 'ai1314')
parameter = pika.ConnectionParameters('localhost',5672,'/',credential)
connection = pika.BlockingConnection(parameter)

channel = connection.channel()

channel.queue_declare('hello')

channel.basic_publish(exchange = '',
                      routing_key = 'hello',
                      body = 'this is second message from PTVS!')

print(" [x] send message")

channel.close()