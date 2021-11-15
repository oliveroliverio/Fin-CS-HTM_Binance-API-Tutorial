from flask import Flask, render_template

# create new flask application, which is a flask object
app = Flask(__name__)

# define routes
@app.route('/')

# define functions for when the route is called into the browser
def index():
    return render_template('index.html')

@app.route('/buy')
def buy():
    return 'buy'

@app.route('/sell')
def sell():
    return 'sell'

@app.route('/settings')
def settings():
    return 'settings'

