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

before running, do this in terminal (this creates the environment variable)

```
export FLASK_APP=app.py
flask run
```

After running, a small webserver built in will run.  Go to browser and type: `localhost:5000`
When `@route('/')` is accessed on the browser, it calls function `hello_world()` . Whatever the function returns is displayed on browser.  Keep this in mind when developing flask applications.