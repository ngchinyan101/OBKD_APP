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

@app.route("/profile", methods=["GET"])
def profile():
    return render_template('profile.html', title='My Profile')

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

# bitcoin section
@app.route('/bitcoin', methods=['GET'])
def bitcoin():
    return render_template('bitcoin.html', title='Bitcoin')

@app.route('/bitcoinresult',methods=['GET', 'POST'])
def bitcoinresult():
    error = None
    if request.method == "POST":
        bitcoinCode = request.form['bitcoinSymbol']
        api_key = 'Y0N5J0ZJLKJACDU2'

        url = "https://www.alphavantage.co/query"

        querystring = {"function":"CURRENCY_EXCHANGE_RATE","from_currency":"BTC","to_currency":"SGD","apikey":api_key}

        headers = {
            'User-Agent': "PostmanRuntime/7.20.1",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "1a946e81-6378-4645-8c4d-3abca68a620a,3d69d650-638a-4903-8350-44a6118afa4e",
            'Host': "www.alphavantage.co",
            'Accept-Encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }
    
        response = requests.request("GET", url, headers=headers, params=querystring)

        bitcoinData = json.loads(response.text)

        fromBitcoinCode = bitcoinData["Realtime Currency Exchange Rate"]["1. From_Currency Code"]

        fromBitcoinName = bitcoinData["Realtime Currency Exchange Rate"]["2. From_Currency Name"]

        toBitcoinCode = bitcoinData["Realtime Currency Exchange Rate"]["3. To_Currency Code"]

        toBitcoinName = bitcoinData["Realtime Currency Exchange Rate"]["4. To_Currency Name"]

        lastRefreshedBitcoinDate = bitcoinData["Realtime Currency Exchange Rate"]["6. Last Refreshed"]

        latestExchangeBitcoinRate = bitcoinData["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
        

    return render_template('bitcoin_rate.html', title='Bitcoin Rate',bFromCode=fromBitcoinCode, bFromName=fromBitcoinName, bToCode=toBitcoinCode, bToName=toBitcoinName ,bCode=bitcoinCode, bRate=latestExchangeBitcoinRate, bTime=lastRefreshedBitcoinDate)


# litecoin section
@app.route('/litecoin', methods=['GET'])
def litecoin():
    return render_template('litecoin.html', title='Litecoin')

@app.route('/litecoinresult',methods=['GET', 'POST'])
def litecoinresult():
    error = None
    if request.method == "POST":
        litecoinCode = request.form['litecoinSymbol']
        api_key = 'Y0N5J0ZJLKJACDU2'

        url = "https://www.alphavantage.co/query"

        querystring = {"function":"CURRENCY_EXCHANGE_RATE","from_currency":"LTC","to_currency":"SGD","apikey":api_key}

        headers = {
            'User-Agent': "PostmanRuntime/7.20.1",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "d744106b-c528-4b1b-99c9-6b386b326d92,f30915b7-80e2-407c-8899-2c7027431493",
            'Host': "www.alphavantage.co",
            'Accept-Encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }
    

        response = requests.request("GET", url, headers=headers, params=querystring)

        litecoinData = json.loads(response.text)

        fromLitecoinCode = litecoinData["Realtime Currency Exchange Rate"]["1. From_Currency Code"]

        fromLitecoinName = litecoinData["Realtime Currency Exchange Rate"]["2. From_Currency Name"]

        toLitecoinCode = litecoinData["Realtime Currency Exchange Rate"]["3. To_Currency Code"]

        toLitecoinName = litecoinData["Realtime Currency Exchange Rate"]["4. To_Currency Name"]

        lastRefreshedLitecoinDate = litecoinData["Realtime Currency Exchange Rate"]["6. Last Refreshed"]

        latestExchangeLitecoinRate = litecoinData["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
        

    return render_template('litecoin_rate.html', title='litecoin Rate', lFromCode=fromLitecoinCode, lFromName=fromLitecoinName, lToCode=toLitecoinCode, lToName=toLitecoinName, lCode=litecoinCode, lRate=latestExchangeLitecoinRate, lTime=lastRefreshedLitecoinDate)

# Ethereum section
@app.route('/ethereum', methods=['GET'])
def ethereum():
    return render_template('ethereum.html', title='Ethereum')

@app.route('/ethereumresult',methods=['GET', 'POST'])
def ethereumresult():
    error = None
    if request.method == "POST":
        ethereumCode = request.form['ethereumSymbol']
        api_key = 'Y0N5J0ZJLKJACDU2'


        url = "https://www.alphavantage.co/query"

        querystring = {"function":"CURRENCY_EXCHANGE_RATE","from_currency":"ETH","to_currency":"SGD","apikey":api_key}

        headers = {
            'User-Agent': "PostmanRuntime/7.20.1",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "049e1368-619e-421c-9a12-c1e496fad888,e8edc3d5-18f1-4faa-befb-f12a7f88b168",
            'Host': "www.alphavantage.co",
            'Accept-Encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }
    

        response = requests.request("GET", url, headers=headers, params=querystring)

        ethereumData = json.loads(response.text)

        fromEthereumCode = ethereumData["Realtime Currency Exchange Rate"]["1. From_Currency Code"]

        fromEthereumName = ethereumData["Realtime Currency Exchange Rate"]["2. From_Currency Name"]

        toEthereumCode = ethereumData["Realtime Currency Exchange Rate"]["3. To_Currency Code"]

        toEthereumName = ethereumData["Realtime Currency Exchange Rate"]["4. To_Currency Name"]

        lastRefreshedEthereumDate = ethereumData["Realtime Currency Exchange Rate"]["6. Last Refreshed"]

        latestExchangeEthereumRate = ethereumData["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
        

    return render_template('ethereum_rate.html', title='Ethereum Rate', eFromCode=fromEthereumCode, eFromName=fromEthereumName, eToCode=toEthereumCode, eToName=toEthereumName, eCode=ethereumCode, eRate=latestExchangeEthereumRate, eTime=lastRefreshedEthereumDate)