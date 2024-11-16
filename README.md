# Final Project (Data Streaming)

## Requirements

- Python 3.11.10 (above versions might pose some problems)
	- python-dotenv
	- kafka-python
- Kafka 3.9.0
- RAPID API account
	- enable Yahoo Finance, copy the API-key
	- Store the key in a .env at the root of the project : RAPIDAPI_KEY="{your-api-key}"

## Description

This project streams real time stock data using the RAPID API, processes it with Kafka, and consumes the data through a Kafka consumer.  

The data (stock price so far) is then aggregated every minute over a 10 minute window.  

## How to run 

On 4 terminal tabs run these commands :

- Start Zookeeper (Kafka needs Zookeeper to run):
```bash
/opt/homebrew/Cellar/kafka/3.9.0/libexec/bin/zookeeper-server-start.sh /opt/homebrew/etc/kafka/zookeeper.properties
```
- Start Kafka Broker:
```bash
/opt/homebrew/Cellar/kafka/3.9.0/libexec/bin/kafka-server-start.sh /opt/homebrew/etc/kafka/server.properties
```
- Run the Consumer (consumes the stock data from Kafka):
```bash
python consumer/stock_data_consumer.py
```
- Run the Producer (produces stock data to Kafka from the Polygon API):
```bash
python producer/stock_data_producer.py
```

Change the above paths according to your kafka installation.

