#!/usr/bin/env python3
""" Configure Babel for translation """

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config():
    """ Simple class """
    LANGUAGES = ["en", "fr"]

    def get_locale(self):
        """ Sets the locale to en and timezone to UTC """
        app.config['BABEL_DEFAULT_LOCALE'] = 'en'
        app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


@app.route('/', strict_slashes=False)
def index():
    """ Index route """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
