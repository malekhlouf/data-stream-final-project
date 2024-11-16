import json
from kafka import KafkaProducer
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'utils')))
from utils.yahoo_finance_api import get_real_time_stock_price

import config
import time

# Create Kafka producer
producer = KafkaProducer(
    bootstrap_servers=config.KAFKA_SERVER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def produce_stock_data():
    stock_symbol = config.STOCK_SYMBOL
    while True:
        stock_data = get_real_time_stock_price(stock_symbol)
        if stock_data:
            print(f"Data received: {stock_data}")
            producer.send(config.KAFKA_TOPIC, stock_data)
            producer.flush()
        time.sleep(config.REQUEST_INTERVAL.total_seconds())  # Request data every 10 seconds

if __name__ == "__main__":
    produce_stock_data()