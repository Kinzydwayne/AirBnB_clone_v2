#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")

#!/usr/bin/python3
"""A script that starts a flask web application
Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask("_name_")


@app.route('/airbnb-onepage/', strict_slashes=False)
def hello():
    """Return a given string"""
    return ("Hello HBNB!")


if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000, debug=False)
