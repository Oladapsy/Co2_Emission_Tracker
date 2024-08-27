#!/usr/bin/python3
from flask import Flask
"""flask module"""


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ dispaly the home page"""
    return render_template('index.html')

@app.route('/home/', strict_slashes=False)
def home():
    """ dispaly the home page"""
    return render_template('index.html')

@app.route('/about_us/', strict_slashes=False)
def home():
    """ dispaly the about page"""
    return render_template('about.html')

@app.route('/contact_us/', strict_slashes=False)
def home():
    """ dispaly the contact page"""
    return render_template('contact.html')

@app.route('/', strict_slashes=False)
def home():
    """ dispaly the page"""
    return render_template('index.html')



