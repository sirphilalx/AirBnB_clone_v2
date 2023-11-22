#!/usr/bin/python3
""" A script that starts a Flask web application """

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """ Display a list of States in a HTML page """
    states = storage.all("State")
    return render_template('9-states.html', state=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """ Display a list of States with info about 'id' if it's present """
    for state in storage.all("State").values():
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')


@app.teardown_appcontext
def teardown(exc):
    """ Removes current SQLAlchemy session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
