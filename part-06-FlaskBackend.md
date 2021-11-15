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
export FLASK_ENV=development
flask run
```

After running, a small webserver built in will run.  Go to browser and type: `localhost:5000`
When `@route('/')` is accessed on the browser, it calls function `hello_world()` . Whatever the function returns is displayed on browser.  Keep this in mind when developing flask applications.

Modify this to return an index page
```python
@app.route('/')
def index():
    return 'index'
```

Add buy, sell, settings routes

```python
@app.route('/buy')
def buy():
    return 'buy'

@app.route('/sell')
def sell():
    return 'sell'

@app.route('/settings')
def settings():
    return 'settings'
```

Now we want to return HTML [jinja templates](jinja.palletsprojects.com/en/2.11.x/)
Add the index.html file to templates folder, and move chart.js to static folder
Also make a data directory
Modified app.py to include render_template module.

Note, when ran, no more chart or other stuff.  (chart.js in different location).  Look at [static files documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/#static-files)

modify This
```html
 <script src='chart.js'></script>
```
to this
```html
<script src="{{ url_for('static', filename='chart.js') }}" />
```