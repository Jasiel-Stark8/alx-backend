#!/usr/bin/env python3
"""Flask App"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


def get_locale():
    """Return default language as en"""
    return request.accept_languages.best_match(['en', 'fr'])


def get_timezone():
    """Get Timezone else default to UTC"""
    return request.timezone

babel = Babel(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.route('/')
def home():
    """Display homme page"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
