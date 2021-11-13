from binance.client import Client
import config

client = Client(API_KEY, API_SECRET)
prices = client.get_all_tickers()
print(prices)