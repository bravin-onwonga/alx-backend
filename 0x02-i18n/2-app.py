#!/usr/bin/env python3
""" Configure Babel for translation """

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config():
    """ Simple class """
    LANGUAGES = ["en", "fr"]

    def get_locale(self):
        """ Sets the locale to en and timezone to UTC """
        BABEL_DEFAULT_LOCALE = 'en'
        BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Best matching language """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """ Index route """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
