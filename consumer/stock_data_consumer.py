import json
from kafka import KafkaConsumer
from utils.sliding_window import add_to_window, slide_window
from config import KAFKA_TOPIC, KAFKA_SERVER

# Initialize the Kafka consumer
consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_SERVER,
    group_id="stock-consumer-group",
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),  # Deserialize JSON data
)


def consume_stock_data():
    for message in consumer:
        stock_data = message.value
        add_to_window(stock_data)
        slide_window()


if __name__ == "__main__":
    consume_stock_data()
