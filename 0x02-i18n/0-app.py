#!/usr/bin/env python3
"""Flask App"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Display homme page"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
