#!/usr/bin/env python3
"""Flask App"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
app.config.from_pyfile('babel.cfg')
babel = Babel(app)

@babel.localeselector
def get_locale():
    # Your locale selection logic (like in previous steps)
    pass

@app.route('/')
def home():
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
