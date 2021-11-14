# Python Binance package
- Authenticate using api key
- then retrieve current candlesticks
- downloading historical data
- run the above through technical analysis libraries (TA-Lib).  Goal is to run TA-lib indicators against datasets to pick out patterns
- Then hook ta-lib to `backtrader` to backtest indicators against historical dataset
- python binance is a wrapper for binance API

Install package
```
pip install python-binance
```
Sign up for binance.us
```
gmail, pz
```

Go to account -> Settings -> API management -> get API and Secret Key -> input in `config.py`

Made a `test` one.  Make sure to make another one for live trades vs paper trades

Make `getData.py` test script to make sure you can get data from api (see python-binance docs)

## 05:00
Lots of different endpoints.  But interested in market data/candlestick data (both current days and historical for backtesting)

[Look at the Get historical KLine function](https://python-binance.readthedocs.io/en/latest/market_data.html#id6)

```python
candles = client.get_klines(symbol='BNBBTC', interval=Client.KLINE_INTERVAL_30MINUTE)
```

[documentation for Kline output](https://binance-docs.github.io/apidocs/futures/en/#compressed-aggregate-trades-list)
It's a list of lists with OHLC

Next step, write candlestick structure information (OHLC, Unix time stamp, no of trades, etc) into a file for backtesting or other.
[Write to CSV](https://docs.python.org/3/library/csv.html).  Note, you want to write a row