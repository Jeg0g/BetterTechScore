from flask import Flask, redirect, render_template, url_for
from parser_1 import parseURL

application = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')

URL="https://scores.hssailing.org/s23/central-mallory-qualifier/rotations/"


@application.route('/')
def index():
    parseURL(URL)
    return render_template('index.html')

@application.route('/diva')
def diva():
    parseURL(URL)
    return render_template('diva.html')

@application.route('/divb')
def divb():
    parseURL(URL)
    return render_template('divb.html')

@application.route('/sailors')
def sailors():
    parseURL(URL)
    return render_template('sailors.html')

if __name__=='__main__':
    application.run(debug = True)
