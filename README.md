# Final Project (Data Streaming)

## Description

This project streams real time stock data using the Rapid API (Yahoo Finance). The Kafka *Producer* sends the data to the *Consumer* which passes it to a *Sliding Window* script to aggregate the data. 

## Requirements

- MacOS or Linux
- Kafka 3.9.0
- Python 3.11.10 (above versions might pose some problems)
	- python-dotenv
	- kafka-python
	- requests
- RAPID API account
	- enable Yahoo Finance, copy the API-key (X-RapidAPI-Key)
	- Store the key in a **.env** file at the root of the project (cf. **.env.template**)

## How to run 

1. Open the **config.py** file and modify it according to your installation and to what you want to observe (stock_symbol, window length, sliding interval, request interval ...).  
  
2. In the **yahoo_finance_api.py** file, uncomment the part for real-time data and comment the testing line.

2. Open a terminal in the root folder of the project and run :  
```bash
python main.py
```

3. To stop the execution of the program type :  
`
Ctrl+C
`
for each window (zookeeper, kafka, and the main window where the aggregation is displayed)