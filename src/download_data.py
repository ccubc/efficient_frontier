import yfinance as yf
import pandas as pd
import yaml

config = yaml.safe_load(open("../config/config.yaml"))
period = config['period']
interval = config['interval']
stocks = config['stocks']

def download_stock_data(symbol, interval, period):
	"""
	Download stock data with ticker = symbol, interval, period
	Save csv file to data/xxx.csv
	"""
	prices = yf.Ticker(symbol).history(period=period, interval=interval)
	if len(prices) > 0:
		result_file = '../data/' + symbol + '.csv'
		prices.to_csv(result_file)
		print(f"Downloaded stock data of {stocks[s]}, data shape {prices.shape}, saved as {result_file}")

for s in stocks.keys():
	try:
		download_stock_data(s, interval, period)
	except Exception as err:
		print(f"Failed to download data for company {stocks[s]}")
		print(str(err))