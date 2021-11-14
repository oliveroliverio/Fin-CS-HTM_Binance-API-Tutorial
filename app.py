from flask import Flask

# create new flask application, which is a flask object
app = Flask(__name__)

# define routes
@app.route('/')

# define functions for when the route is called into the browser
def hello_world():
    return 'Hello, World!'