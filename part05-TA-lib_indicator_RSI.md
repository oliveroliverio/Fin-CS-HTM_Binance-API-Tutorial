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


Makes an array of arrays

```
[[1.63646010e+12 6.73537400e+04 6.75632800e+04 ... 2.34429830e+02
  1.58027108e+07 0.00000000e+00]
 [1.63646100e+12 6.75010100e+04 6.77318600e+04 ... 2.32645630e+02
  1.57262539e+07 0.00000000e+00]
 [1.63646190e+12 6.76818700e+04 6.76889200e+04 ... 1.02389910e+02
  6.91771869e+06 0.00000000e+00]
 ...
 [1.63690740e+12 6.41500000e+04 6.42110000e+04 ... 2.31148700e+02
  1.47687132e+07 0.00000000e+00]
 [1.63690830e+12 6.36911900e+04 6.38143600e+04 ... 2.09495930e+02
  1.33358198e+07 0.00000000e+00]
```
but we only want the closing values (the 4th value). How to extract that? [Look here](https://stackoverflow.com/questions/25614749/how-to-import-csv-file-as-numpy-array-in-python).  "numpy.genfromtxt"

```python
close = my_data[:,4]
print(close)
```

output
```
(base) oliveroliverio@Olivers-MacBook-Pro Fin-CS-HTM_Binance-API-Tutorial % python ta.py
[67501.   67681.86 67550.01 67766.21 67716.01 67800.   68080.37 67893.7
 67785.24 67880.01 67333.53 67102.94 67035.99 66905.   66771.1  66543.59
 66767.85 66943.24 66693.   66424.29 66529.   66857.01 66810.21 67015.96
 66799.99 66740.   66520.37 66354.09 66607.48 66613.85 66800.21 66732.16
 67023.21 67314.74 67348.99 67447.   67389.77 67542.36 67721.   67511.
 67000.   67246.49 67292.72 67188.55 67300.97 67160.48 66947.66 67107.35
 67282.97 66882.09 66996.82 67103.9  67168.51 67250.42 67018.36 67079.15
 67078.72 66821.47 66815.32 66462.06 66369.3  66401.01 66487.23 66345.99
```

This looks right.  Now apply RSI function to this numpy array
```python
rsi = talib.RSI(close)
```

output
```
(base) oliveroliverio@Olivers-MacBook-Pro Fin-CS-HTM_Binance-API-Tutorial % python ta.py
[        nan         nan         nan         nan         nan         nan
         nan         nan         nan         nan         nan         nan
         nan         nan 35.05699592 31.86071302 37.87359586 42.17157418
 38.11954725 34.30753879 36.95334005 44.49485407 43.69180897 48.12453441
 44.19192807 43.13744771 39.42808959 36.84490858 42.97603989 43.12552032
 47.46440922 46.08195085 52.45973397 57.83926131 58.43434649 60.16698742
 58.6301325  61.45701018 64.51415076 58.62715039 47.31333833 52.11380634
 52.97913832 50.75356237 53.04599092 49.91868315 45.5389028  49.1444992
 52.84214812 44.82948962 47.29276892 49.55651541 50.92608577 52.68014612
 47.50007015 48.91710712 48.90705136 43.18724555 43.05759809 36.31406605
 34.7739868  35.77670969 38.5431838  35.82106586 39.40703247 43.00331324
```

Note: under 30 = oversold (looking before this you expect to see prices decreases quickly), over 30 = overbought (looking before this you expect prices to be rising quickly)

Check this by getting the unix time stamp, going [here](https://unixtimestamp.com/index.php) to figure out the actual date.  Go to tradingview.com and load RSI indicator on the ticker symbol.