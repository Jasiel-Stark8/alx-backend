#!/usr/bin/env python3
"""Flask App"""

from flask import Flask, render_template, g, request
from flask_babel import Babel

app = Flask(__name__)

class Config(object):
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)


# def get_locale():
#     """Return default language as en"""
#     return request.accept_languages.best_match(['en', 'fr'])


# def get_timezone():
#     """Get Timezone else default to UTC"""
#     user = getattr(g, 'user', None)
#     if user is not None:
#         return user.timezone
#     return 'UTC'


babel = Babel(app)


@app.route('/')
def home():
    """Display homme page"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
