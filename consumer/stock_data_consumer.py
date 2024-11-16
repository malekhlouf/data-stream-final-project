from kafka import KafkaConsumer
import json
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))
from utils.sliding_window import add_to_window, slide_window
import config

# Initialize the Kafka consumer
consumer = KafkaConsumer(
    config.KAFKA_TOPIC,
    bootstrap_servers=config.KAFKA_SERVER,
    group_id="stock-consumer-group",
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))  # Deserialize JSON data
)

def consume_stock_data():
    for message in consumer:
        stock_data = message.value
        add_to_window(stock_data)
        slide_window()

if __name__ == "__main__":
    consume_stock_data()