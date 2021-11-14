import numpy 
import talib
from numpy import genfromtxt

my_data = genfromtxt('15minutes.csv', delimiter=',')
close = my_data[:,4]
print(close)
