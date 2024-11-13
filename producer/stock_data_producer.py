import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from kafka import KafkaProducer
import json
import time
from utils.polygon_api import get_stock_data  # Adjust the import path if needed
from config.kafka_config import KAFKA_BROKER, KAFKA_TOPIC  # Adjust the import path if needed

# Create Kafka producer
def create_producer():
    return KafkaProducer(
        bootstrap_servers=KAFKA_BROKER,
        value_serializer=lambda x: json.dumps(x).encode('utf-8')  # Serialize data as JSON
    )

# Function to fetch stock data and produce to Kafka
def produce_stock_data():
    producer = create_producer()
    while True:
        stock_data = get_stock_data()  # Fetch stock data from Polygon API
        print("Sending data to Kafka...\n\n")  # Log the stock data
        producer.send(KAFKA_TOPIC, value=stock_data)  # Send data to Kafka topic
        time.sleep(30)  # Wait for 30 seconds before fetching the next set of data

if __name__ == "__main__":
    produce_stock_data()  # Start producing stock data to Kafka