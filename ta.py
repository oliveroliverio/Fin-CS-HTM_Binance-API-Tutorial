import numpy 
import talib

close = numpy.random.random(100)
print(close)

moving_average = talib.SMA(close)
print(moving_average)