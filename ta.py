import numpy 
import talib

close = numpy.random.random(100)
print(close)

# changed to 10day MA
moving_average = talib.SMA(close, timeperiod=10)
# print(moving_average)

rsi = talib.RSI(close)
print(rsi)