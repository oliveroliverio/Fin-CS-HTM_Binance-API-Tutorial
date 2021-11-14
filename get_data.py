from binance.client import Client
import config2
import csv

client = Client(config2.API_KEY, config2.API_SECRET)

csvFile = open('2012-2020.csv', 'w', newline='')

# file handler
candlestick_writer = csv.writer(csvFile, delimiter=',')

# get candlestick info from binance client
candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_30MINUTE, "1 Dec, 2012", "1 Jan, 2020")

for candlestick in candlesticks:
  candlestick_writer.writerow(candlestick)

csvFile.close()