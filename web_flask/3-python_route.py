#!/usr/bin/python3
""" A script that starts a Flask web application """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Displays string 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Displays string 'HBNB!'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Displays 'C' and the value of <text> """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """ Displays 'Python' and the value of the text variable """
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)