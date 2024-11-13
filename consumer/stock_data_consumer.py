from kafka import KafkaConsumer
import json
import logging

# Set up logging to track what the consumer is doing
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

# Kafka configurations
KAFKA_BROKER = "localhost:9092"  # Update if your Kafka broker is on a different address
KAFKA_TOPIC = "stock_data"  # The topic where the stock data is being produced

# Initialize Kafka consumer
consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_BROKER,
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),  # Deserialize message from JSON
    auto_offset_reset='earliest',  # Start reading at the earliest message in the topic
    group_id="stock_data_group"  # Consumer group (useful for handling multiple consumers)
)

def consume_stock_data():
    """Consumes stock data messages from Kafka."""
    logger.info("Consumer started, waiting for messages...\n")
    for message in consumer:
        # Each message received is a Kafka message
        stock_data = message.value
        print(f"\nReceived stock data: {stock_data}\n")
        # logger.info(f"Received stock data: {stock_data}\n")
        # Here you can process the stock data further (e.g., visualize, store in a database, etc.)

if __name__ == "__main__":
    consume_stock_data()