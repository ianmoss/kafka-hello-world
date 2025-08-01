from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')

topic = 'hello-world'

for i in range(10):
    message = f"Hello Kafka {i}".encode('utf-8')
    producer.send(topic, message)
    print(f"> Sent: {message.decode()}")
    time.sleep(1)

producer.flush()
producer.close()
