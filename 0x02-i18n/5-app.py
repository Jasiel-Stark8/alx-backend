#!/usr/bin/env python3
"""Flask App"""

from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id: int):
    """Return a user dictionary or None"""
    return users.get(user_id)


@app.before_request
def before_request():
    """Set a user as a global variable"""
    user_id = request.args.get('login_as', type=int)
    g.user = get_user(user_id)


@babel.localeselector
def get_locale():
    """Get locale from user preferences or request headers"""
    user = getattr(g, 'user', None)
    if user is not None:
        return user.get('locale')
    return request.accept_languages.best_match(['en', 'fr'])


@app.route('/')
def home():
    """Return home page"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
