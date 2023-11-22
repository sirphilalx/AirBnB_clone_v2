#!/usr/bin/python3
""" A script that starts a Flask web application """

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ Displays a HTML page """
    state = storage.all("State")
    amenity = storage.all("Amenity")
    return render_template('10-hbnb_filters.html', states=state,
                           amenities=amenity)


@app.teardown_appcontext
def teardown(exc):
    """ Removes current SQLAlchemy session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
