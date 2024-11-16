# config.py
from datetime import timedelta
KAFKA_TOPIC = "stock_data"
KAFKA_SERVER = "localhost:9092"
STOCK_SYMBOL = "AAPL"
WINDOW_LENGTH = timedelta(minutes=10)  # 10-minute window
SLIDING_LENGTH = timedelta(seconds=60)   # Slide window every 60 seconds
REQUEST_INTERVAL = timedelta(seconds=30)  # Request data every 30 seconds
