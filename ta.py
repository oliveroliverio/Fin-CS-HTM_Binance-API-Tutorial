import numpy 
import talib

close = numpy.random.random(100)
print(close)

# uses 30 day MA by default
moving_average = talib.SMA(close)
print(moving_average)