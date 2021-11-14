from binance.client import Client
import config2

client = Client(config2.API_KEY, config2.API_SECRET)
# prices = client.get_all_tickers()
# # print(prices)

# for price in prices:
#   print(price)

candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)

for candlestick in candles:
  print(candlestick)

print(len(candles))
# output is 500 50min candlesticks