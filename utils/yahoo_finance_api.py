import os
import requests
from dotenv import load_dotenv
from config import STOCK_SYMBOL

load_dotenv()

def get_real_time_stock_price(symbol: str):
    api_key = os.getenv("RAPIDAPI_KEY")
    if not api_key:
        raise EnvironmentError("RAPIDAPI_KEY not found in environment variables")
    
    ## Uncomment for true real-time data : 
    # url = f"https://yahoo-finance166.p.rapidapi.com/api/stock/get-price?region=US&symbol={symbol}"
    # headers = {
    #     'x-rapidapi-host': 'yahoo-finance166.p.rapidapi.com',
    #     'x-rapidapi-key': api_key
    # }

    # response = requests.get(url, headers=headers)
    
    # if response.status_code == 200:
    #     data = response.json()
    #     return data
    # else:
    #     print(f"Error fetching data: {response.status_code}")
    #     return None

    ## For testing Purposes only (free plan only 500 requests/month):
    return {'quoteSummary': {'result': [{'price': {'maxAge': 1, 'preMarketChange': {}, 'preMarketPrice': {}, 'preMarketSource': 'FREE_REALTIME', 'postMarketChangePercent': {'raw': 0.00120002, 'fmt': '0.12%'}, 'postMarketChange': {'raw': 0.270004, 'fmt': '0.27'}, 'postMarketTime': 1731718799, 'postMarketPrice': {'raw': 225.27, 'fmt': '225.27'}, 'postMarketSource': 'FREE_REALTIME', 'regularMarketChangePercent': {'raw': -0.014109198, 'fmt': '-1.41%'}, 'regularMarketChange': {'raw': -3.2200012, 'fmt': '-3.22'}, 'regularMarketTime': 1731704401, 'priceHint': {'raw': 2, 'fmt': '2', 'longFmt': '2'}, 'regularMarketPrice': {'raw': 225, 'fmt': '225.00'}, 'regularMarketDayHigh': {'raw': 226.92, 'fmt': '226.92'}, 'regularMarketDayLow': {'raw': 224.27, 'fmt': '224.27'}, 'regularMarketVolume': {'raw': 46862701, 'fmt': '46.86M', 'longFmt': '46,862,701.00'}, 'averageDailyVolume10Day': {}, 'averageDailyVolume3Month': {}, 'regularMarketPreviousClose': {'raw': 228.22, 'fmt': '228.22'}, 'regularMarketSource': 'FREE_REALTIME', 'regularMarketOpen': {'raw': 225.92, 'fmt': '225.92'}, 'strikePrice': {}, 'openInterest': {}, 'exchange': 'NMS', 'exchangeName': 'NasdaqGS', 'exchangeDataDelayedBy': 0, 'marketState': 'CLOSED', 'quoteType': 'EQUITY', 'symbol': 'AAPL', 'underlyingSymbol': None, 'shortName': 'Apple Inc.', 'longName': 'Apple Inc.', 'currency': 'USD', 'quoteSourceName': 'Nasdaq Real Time Price', 'currencySymbol': '$', 'fromCurrency': None, 'toCurrency': None, 'lastMarket': None, 'volume24Hr': {}, 'volumeAllCurrencies': {}, 'circulatingSupply': {}, 'marketCap': {'raw': 3401054945280, 'fmt': '3.40T', 'longFmt': '3,401,054,945,280.00'}}}], 'error': None}}

if __name__ == "__main__":
    get_real_time_stock_price(STOCK_SYMBOL)