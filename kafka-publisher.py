from confluent_kafka import Producer
import json

topic = 'my-topic'

message = {
    'name': 'John Doe',
    'age': 228,
    'email': 'johndoe@gmail.com'
}
json_message = json.dumps(message)

conf = {
    'bootstrap.servers': 'localhost:9092',
#    'client.id': 'my-producer'
}

producer = Producer(conf)
producer.produce(topic, key=None, value=json_message)
producer.flush()
