from flask import Flask, redirect, render_template, url_for
from parser_1 import Parser_1

application = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')

URL="https://scores.hssailing.org/f22/2022-atlantic-coast/full-scores/"

p=Parser_1(URL)

@application.route('/')
def index():
    p.parseURL()
    return render_template('index.html')

@application.route('/diva')
def diva():
    p.parseURL()
    return render_template('diva.html')

@application.route('/divb')
def divb():
    p.parseURL()
    return render_template('divb.html')

if __name__=='__main__':
    application.run(debug = False)
