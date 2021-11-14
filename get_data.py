from binance.client import Client
import config2

client = Client(config2.API_KEY, config2.API_SECRET)
# prices = client.get_all_tickers()
# # print(prices)

# for price in prices:
#   print(price)

candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)

csvFile = open('15minutes.csv', 'w', newline='')

candlestick_writer = csv.writer(csvFile, delimiter=',')


for candlestick in candles:
  # print(candlestick)
  candlestick_writer.writerow(candlestick)

# print(len(candles))
# output is 500 50min candlesticks