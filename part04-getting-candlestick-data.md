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

