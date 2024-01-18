#!/usr/bin/env python3
"""Flask App"""

from flask import Flask, render_template, g, request
from flask_babel import Babel


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
    url_locale = request.args.get('locale')
    if url_locale and url_locale in Config.LANGUAGES:
        return url_locale
    user = getattr(g, 'user', None)
    if user is not None and user.get('locale') in Config.LANGUAGES:
        return user.get('locale')
    return request.accept_languages.best_match(Config.LANGUAGES)


# before_request decorator
@app.before_request
def before_request():
    """"""
    user_id = login_as()
    g.user = get_user(users, int(user_id)) if user_id else None
        

@app.route('/')
def home():
    """Return home page"""
    return render_template('5-index.html')


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def login_as():
    """Login as a user in mock schema"""
    user_id = request.args.get('id')
    return int(user_id) if user_id and user_id.isdigit() and int(user_id) in users else None


def get_user(users, user_id: int):
    """User mock login"""
    return users.get(user_id)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
