#!/usr/bin/env python3
"""Flask App"""

from flask import Flask, render_template, g, request
from flask_babel import Babel
from typing import Union, Dict, Integer, String
from functools import wrapper


class Config(object):
    """Babel Config Class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Get locale"""
    # Get locale from URL parameter
    url_locale = request.args.get('locale')
    if url_locale and url_locale in Config.LANGUAGES:
        return url_locale

    # Check User-specific locale preference
    user = getattr(g, 'user', None)
    if user is not None and user.locale in Config.LANGUAGES:
        return user.locale
    return request.accept_languages.best_match(Config.LANGUAGES)


# before_request decorator
@app.before_request
def before_request():
    """"""
    user_id = request.args.get('login_as')
    if user_id:
        g.user = get_user(users, int(user_id))
    else:
        g.user = None
        

@app.route('/')
def home():
    """Return home page"""
    return render_template('3-index.html')


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def login_as() -> Union[Integer, String]:
    """Login as a user in mock schema"""
    user_id = request.args.get('id')
    if user_id in users[id]:
        return user_id
    return 'User not found'

def get_user(users, user_id: int) -> Union[Dict, None]:
    """User mock login"""
    valid_login = login_as(user_id)
    if valid_login:
        if user_id is not None:
            return users[user_id]
    return None


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
