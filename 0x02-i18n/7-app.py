#!/usr/bin/env python3
""" Basic Flask app"""
from flask import Flask, render_template, g, request
from flask_babel import Babel
import pytz


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
    """Determine the best match with our supported languages"""
    # Check URL parameters
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    # Check user settings
    user = get_user()
    if user and 'locale' in user and user['locale'] in app.config['LANGUAGES']:
        return user['locale']
    # Check request headers
    locale = request.accept_languages.best_match(app.config['LANGUAGES'])
    if locale:
        return locale
    # Default locale
    return app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone():
    """Determine the best match with our supported timezones"""
    # Check URL parameters
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    # Check user settings
    user = get_user()
    if user and 'timezone' in user:
        try:
            pytz.timezone(user['timezone'])
            return user['timezone']
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    # Default timezone
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index():
    """Returns index.html"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
