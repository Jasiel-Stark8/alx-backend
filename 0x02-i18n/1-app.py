#!/usr/bin/env python3
"""Flask App"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = ["en", "fr"]
babel = Babel(app)


def get_locale():
    return babel.



@app.route('/')
def home():
    """Display homme page"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
