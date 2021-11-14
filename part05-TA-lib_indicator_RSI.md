# instalation of TA-lib
- unsuccessful on M1 MBA.  
- now working on MBP
- [TA-lib examples](https://mrjbq7.github.io/ta-lib/)

# testing TA-lib
Add requirements.txt
```
python-binance
TA-Lib
numpy
```
Make `ta.py` file
```python
import numpy
import talib

close = numpy.random.random(100)
print(close)
```

This generates a numpy array of random numbers.  [Python lists vs numpy arrays](https://webcourses.ucf.edu/courses/1249560/pages/python-lists-vs-numpy-arrays-what-is-the-difference)

Goal is to make numpy array of closing BTC prices or S&P500 as a sequence of values, which then can be operated on by TA-Lib and perform calculations for us.

Try example: SMA and RSI

```
output = talib.SMA(close)
```

These aren't interesting since they're random numbers.
Next, apply TA-lib to historical data (15min.csv)
Google ["how to read CSV data into numpy array"](https://intellipaat.com/community/9398/how-do-i-read-csv-data-into-a-record-array-in-numpy)
