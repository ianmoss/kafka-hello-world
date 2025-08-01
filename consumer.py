from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'hello-world',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='hello-group'
)

print("Listening for messages...")

for message in consumer:
    print(f"< Received: {message.value.decode()}")
