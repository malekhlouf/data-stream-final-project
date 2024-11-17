from datetime import timedelta

# Set the paths according to your installation.
ZOOKEEPER_SERVER_START = (
    "/opt/homebrew/Cellar/kafka/3.9.0/libexec/bin/zookeeper-server-start.sh"
)
ZOOKEEPER_PROPERTIES = "/opt/homebrew/etc/kafka/zookeeper.properties"
ZOOKEEPER_HOST = "localhost"
ZOOKEEPER_PORT = 2181

# Set the paths according to your installation.
KAFKA_SERVER_START = (
    "/opt/homebrew/Cellar/kafka/3.9.0/libexec/bin/kafka-server-start.sh"
)
KAFKA_SERVER_PROPERTIES = "/opt/homebrew/etc/kafka/server.properties"
KAFKA_HOST = "localhost"
KAFKA_PORT = 9092
KAFKA_TOPIC = "stock_data"
KAFKA_SERVER = "localhost:9092"

# Set the stock symbol according to the stock you want to check.
STOCK_SYMBOL = "AAPL"

REQUEST_INTERVAL = timedelta(seconds=5)  # Request data from api every x (seconds/minutes/days)
# Set these to modify the sliding-window lengths.
WINDOW_LENGTH = timedelta(minutes=10)  # window length (seconds/minutes/days)
SLIDING_LENGTH = timedelta(seconds=10)  # Slide window every x (seconds/minutes/days)
