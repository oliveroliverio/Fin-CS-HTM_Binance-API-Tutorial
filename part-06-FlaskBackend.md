# Making a flask backend
update requirements file

```
python-binance
TA-Lib
numpy
backtrader
flask
```

## Install backtrader
```
pip3 install backtrader
```

Copy [Flask quick start example](https://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart) to `app.py` and work off of this.

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```