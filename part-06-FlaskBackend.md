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
<script src="{{ url_for('static', filename='chart.js') }}"></script>
```

Now it'll load the chart.

## Displaying variables in templates
use the brackets: `{{ variable name }}`

Say you want to change the title of application.  Modify the def function from this
```python
def index():
  return render_template('index.html')
```
to this
```python
def index():
  title = 'CoinView'
  return render_template('index.html', title=title)
```
Then modify the html template from this:
```html
<body>
  <h2>Trades</h2>
  <div id="chart"></div>
  <div id="trades"></div>
```
to this:

```html
<body>
  <h2>{{ title }}</h2>
  <div id="chart"></div>
  <div id="trades"></div>
```

If you want to save settings to a database (like the 14 on the RSI if the user makes that a favorite).  We retrieve these values from db when the page reloads, send over to the template, then display in template, that way different users of the webapp can have different settings for their own.

Next we'll add logic to this template to interact with cryptocurrency data and binance api