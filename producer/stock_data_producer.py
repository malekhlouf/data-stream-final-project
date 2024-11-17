import json
import time
from kafka import KafkaProducer
from datetime import datetime
from utils.yahoo_finance_api import get_real_time_stock_price
from config import STOCK_SYMBOL, KAFKA_SERVER, KAFKA_TOPIC, REQUEST_INTERVAL


# Create Kafka producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)


def produce_stock_data():
    while True:
        stock_data = get_real_time_stock_price(STOCK_SYMBOL)
        if stock_data:
            current_time = datetime.utcnow()
            print(f"{current_time}: Data received from API.\n")
            producer.send(KAFKA_TOPIC, stock_data)
            producer.flush()
        time.sleep(REQUEST_INTERVAL.total_seconds())  # Request data every x seconds


if __name__ == "__main__":
    produce_stock_data()
