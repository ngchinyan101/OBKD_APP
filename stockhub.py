from requests_oauthlib import OAuth2Session
from flask import Flask, request, redirect, session, url_for, render_template
from requests.auth import HTTPBasicAuth
import requests
import json

app = Flask(__name__)

@app.route("/")
@app.route("/homepage")

def homepage():
    return render_template('home_page.html', title='Home')

@app.route("/usequities", methods=["GET"])
def usequities():
    return render_template('usequities.html', title='U.S. Equities')

@app.route("/sgequities", methods=["GET"])
def sgequities():
    return render_template('sgequities.html', title='SG Equities')

@app.route("/fx", methods=["GET"])
def fx():
    return render_template('fx.html', title='Foreign Exchange')

@app.route("/cryptocurrency", methods=["GET"])
def cryptocurrency():
    return render_template('cryptocurrency.html', title='Crptocurrency')

@app.route("/preciousmetal", methods=["GET"])
def preciousmetal():
    return render_template('preciousmetal.html', title='Precious Metal')

@app.route("/crudeoil", methods=["GET"])
def crudeoil():
    return render_template('crudeoil.html', title='Crude Oil')

@app.route("/hello", methods=["GET"])
def hello():
    return render_template('hello.html', title='Crude Oil')

if __name__ == '___main__': 
    app.run(debug=True)