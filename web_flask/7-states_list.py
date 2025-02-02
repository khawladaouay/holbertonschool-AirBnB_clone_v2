#!/usr/bin/python3
"""7-states_list Module"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list():
    states = storage.all(State).values()
    return render_template('7-states_list.html', my_dict=states)


@app.teardown_appcontext
def close_sqlalchemy(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
