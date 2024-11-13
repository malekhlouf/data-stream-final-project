import requests
import os
from dotenv import load_dotenv
import time

# Load environment variables from .env
load_dotenv()

# Function to fetch stock data with a 30-second delay between requests
def get_stock_data():
    api_key = os.getenv("POLYGON_API_KEY")
    url = f"https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2023-01-09/2023-01-09?apiKey={api_key}"
    
    while True:
        print(f"Requesting...")
        response = requests.get(url)
        
        if response.status_code == 200:
            print("Data fetched:", response.json())
            return response.json()  # Return the stock data if the request is successful
        
        elif response.status_code == 429:
            # If rate limit is exceeded, print the response and retry after 30 seconds
            print("Rate limit exceeded. Response:", response.json())
            print("Retrying in 30 seconds...")
            time.sleep(30)  # Wait for 30 seconds before retrying
        
        else:
            # For any other errors, raise an exception
            print(f"Error fetching data: {response.status_code}. Response: {response.json()}")
            raise Exception(f"Error fetching data: {response.status_code}")
        
        # Wait for 30 seconds before making another request, regardless of the response
        print("Waiting 30 seconds before next request...")
        time.sleep(30)