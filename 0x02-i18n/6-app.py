#!/usr/bin/env python3
""" Basic Flask app"""
from flask import Flask, render_template, g, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Get the current user from the users table"""
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


@app.before_request
def before_request():
    """Set the current user before each request"""
    g.user = get_user()


class Config:
    """Language and time configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Determine the best match for the user's locale."""
    # If a user is logged in, use the locale from the user settings
    if g.user is not None:
        return g.user.get('locale')

    # If the 'locale' parameter is given in the URL, use it
    url_locale = request.args.get('locale')
    if url_locale:
        return url_locale

    # Otherwise, use the Accept-Language header in the request
    return request.accept_languages.best_match(['fr', 'en'])



@app.route('/')
def index():
    """Returns index.html"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
