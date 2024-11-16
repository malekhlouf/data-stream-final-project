from collections import deque
from datetime import datetime, timedelta
import logging
from config import WINDOW_LENGTH, SLIDING_LENGTH

# Set up logging for the sliding window
logger = logging.getLogger(__name__)

# Initialize the sliding window (a deque to store stock data)
window = deque()  # Stores (timestamp, stock_data) tuples
last_slide_time = datetime.utcnow()


def add_to_window(stock_data):
    """Add new stock data to the window."""
    current_time = datetime.utcnow()
    # Add the new stock data to the window
    window.append((current_time, stock_data))
    # Remove data older than the sliding window size (2 minutes)
    while window and window[0][0] < current_time - WINDOW_LENGTH:
        window.popleft()


def aggregate_window_data():
    """Aggregate data in the sliding window (calculate the mean price over the last 2 minutes)."""
    if len(window) == 0:
        return None  # No data to aggregate

    count = 0
    avg_close_price = 0
    for _, stock_data in window:
        count += 1
        avg_close_price += stock_data["quoteSummary"]["result"][0]["price"][
            "regularMarketPrice"
        ]["raw"]
    avg_close_price = avg_close_price / count if count > 0 else 0
    
    return {"avg_close_price": avg_close_price, "data_points": count}


def slide_window():
    """Check if it's time to aggregate data, and slide the window if needed."""
    global last_slide_time

    current_time = datetime.utcnow()

    # If it's time to aggregate and log the window data
    if current_time - last_slide_time >= SLIDING_LENGTH:
        print(f"\nAggregating data at {current_time}...")
        aggregated_data = aggregate_window_data()
        if aggregated_data:
            print(f"\nAggregated Data (Last 2 Minutes): {aggregated_data}\n")
        else:
            print("\nNo data available for aggregation.\n")

        last_slide_time = current_time
