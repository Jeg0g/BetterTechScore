from flask import Flask, redirect, render_template, url_for
from parser_1 import Parser_1

app = Flask(__name__)



app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')

URL="https://scores.hssailing.org/s23/mdisa-ssa-team-race/full-scores/"

p=Parser_1(URL)

@app.route('/')
def index():
    p.parseURL()
    return render_template('index.html')

@app.route('/diva')
def diva():
    p.parseURL()
    return render_template('diva.html')

@app.route('/divb')
def divb():
    p.parseURL()
    return render_template('divb.html')

if __name__=='__main__':
    app.run(debug = True)
