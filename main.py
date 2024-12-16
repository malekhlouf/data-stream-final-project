import sys, os
import time
import signal
import socket
import subprocess
from config import (
    ZOOKEEPER_SERVER_START,
    ZOOKEEPER_PROPERTIES,
    ZOOKEEPER_HOST,
    ZOOKEEPER_PORT,
    KAFKA_SERVER_START,
    KAFKA_SERVER_PROPERTIES,
    KAFKA_HOST,
    KAFKA_PORT,
)

# Set the project root path (optional)
project_root = os.path.abspath(os.path.dirname(__file__))
env = os.environ.copy()
env["PYTHONPATH"] = project_root  # If needed to ensure all modules are found

# Store the subprocesses so we can terminate them later
processes = []


def is_zookeeper_ready():
    """Check if Zookeeper is listening on port ZOOKEEPER_PORT."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    try:
        sock.connect((ZOOKEEPER_HOST, ZOOKEEPER_PORT))
        return True
    except socket.error:
        return False
    finally:
        sock.close()


def start_zookeeper():
    """Start Zookeeper in a new terminal tab or window and wait for it to be ready."""
    print("Starting Zookeeper in a new terminal...")
    if sys.platform == "darwin":  # macOS
        os.system(f"osascript -e 'tell application \"Terminal\" to do script \"{ZOOKEEPER_SERVER_START} {ZOOKEEPER_PROPERTIES}\"'")
    elif sys.platform == "linux" or sys.platform == "linux2":  # Linux
        os.system(f"gnome-terminal -- bash -c '{ZOOKEEPER_SERVER_START} {ZOOKEEPER_PROPERTIES}; exec bash'")
    else:
        print("Unsupported platform for opening new terminal tabs")

    # Wait for Zookeeper to be ready
    while not is_zookeeper_ready():
        time.sleep(1)

    print("Zookeeper is ready!")


def is_kafka_ready():
    """Check if Kafka is listening on port KAFKA_PORT."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    try:
        sock.connect((KAFKA_HOST, KAFKA_PORT))
        return True
    except socket.error:
        return False
    finally:
        sock.close()


def start_kafka():
    """Start Kafka in a new terminal tab or window and wait for it to be ready."""
    print("Starting Kafka in a new terminal...")
    if sys.platform == "darwin":  # macOS
        os.system(f"osascript -e 'tell application \"Terminal\" to do script \"{KAFKA_SERVER_START} {KAFKA_SERVER_PROPERTIES}\"'")
    elif sys.platform == "linux" or sys.platform == "linux2":  # Linux
        os.system(f"gnome-terminal -- bash -c '{KAFKA_SERVER_START} {KAFKA_SERVER_PROPERTIES}; exec bash'")
    else:
        print("Unsupported platform for opening new terminal tabs")

    # Wait for Kafka to be ready
    while not is_kafka_ready():
        time.sleep(1)

    print("Kafka is ready!")


def start_producer():
    """Start the producer to request data and send it to Kafka."""
    producer = subprocess.Popen(["python", "producer/stock_data_producer.py"], env=env)
    processes.append(producer)


def start_consumer():
    """Start the consumer to consume data and process it with the sliding window."""
    consumer = subprocess.Popen(["python", "consumer/stock_data_consumer.py"], env=env)
    processes.append(consumer)


def terminate_processes(signum, frame):
    """Terminate all subprocesses on keyboard interrupt (Ctrl+C)."""
    print("Received Ctrl+C, terminating processes...")
    for process in processes:
        process.terminate()
    sys.exit(0)


if __name__ == "__main__":
    # Register the signal handler for Ctrl+C
    signal.signal(signal.SIGINT, terminate_processes)

    # Start Zookeeper, Kafka, Producer, and Consumer in parallel
    print("Starting Zookeeper...")
    start_zookeeper()

    print("Starting Kafka...")
    start_kafka()

    print("Starting Consumer...")
    start_consumer()

    print("Starting Producer...\n")
    start_producer()

    for process in processes:
        process.wait()
