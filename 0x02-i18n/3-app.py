#!/usr/bin/env python3
"""Flask App"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Get locale"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    """Return home page"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
