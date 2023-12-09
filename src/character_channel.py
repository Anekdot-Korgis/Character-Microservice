import pika

class CharacterChannel:
   def __init__(self, host, username, password):
       self.host = host
       self.username = username
       self.password = password
       self.connection = None
       self.channel = None

   def connect(self):
       credentials = pika.PlainCredentials(self.username, self.password)
       parameters = pika.ConnectionParameters(self.host, 5672, '/', credentials)
       self.connection = pika.BlockingConnection(parameters)
       self.channel = self.connection.channel()

   def close(self):
       self.connection.close()

   def send_message(self, queue_name, message):
       self.channel.basic_publish(exchange='', routing_key=queue_name, body=message)

   def receive_message(self, queue_name, callback):
       self.channel.basic_consume(queue=queue_name, on_message_callback=callback)
       self.channel.start_consuming()
