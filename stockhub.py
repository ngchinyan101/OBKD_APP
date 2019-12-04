from flask import Flask, request, redirect, session, url_for, render_template, flash
from requests_oauthlib import OAuth2Session
from forms import RegistrationForm, LoginForm
from requests.auth import HTTPBasicAuth
from newsapi.newsapi_client import NewsApiClient
import requests
import json

app = Flask(__name__)

app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = '031e8b93c90984f2c4a8bf0d0b7b3360'

client_id = "8d7f7404c85cca13"
client_secret = "031e8b93c90984f2c4a8bf0d0b7b3360"

authorization_base_url = 'https://apm.tp.sandbox.fidor.com/oauth/authorize'
token_url = 'https://apm.tp.sandbox.fidor.com/oauth/token'
redirect_uri = 'http://localhost:5000/callback'

newsapi = NewsApiClient(api_key='158a2c8a3e7b4f7daab8bc350178c1a3')


@app.route("/")
@app.route("/homepage")
def homepage():
    session_var_value = session.get('key')
    return render_template('home_page.html', title='Home', ses=session_var_value)


@app.route("/sgequities", methods=["GET"])
def sgequities():
    session_var_value = session.get('key')
    return render_template('sgequities.html', title='SG Equities', ses=session_var_value)


@app.route("/fx", methods=["GET"])
def fx():
    session_var_value = session.get('key')
    return render_template('fx.html', title='Foreign Exchange', ses=session_var_value)


@app.route("/cryptocurrency", methods=["GET"])
def cryptocurrency():

    session_var_value = session.get('key')
    return render_template('cryptocurrency.html', title='Crptocurrency', ses=session_var_value)


@app.route("/preciousmetal", methods=["GET"])
def preciousmetal():
    session_var_value = session.get('key')
    return render_template('preciousmetal.html', title='Precious Metal', ses=session_var_value)


@app.route("/crudeoil", methods=["GET"])
def crudeoil():
    session_var_value = session.get('key')
    return render_template('crudeoil.html', title='Crude Oil', ses=session_var_value)


@app.route("/cryptocurrencyindex", methods=["GET"])
def cryptocurrencyindex():
    session_var_value = session.get('key')
    return render_template('cryptocurrencyindex.html', title='Purchase of Cryptocurrency', ses=session_var_value)

# @app.route("/gold", methods=["GET"])
# def gold(): 
#     session_var_value = session.get('key')
#     return render_template('gold.html', title='Gold', ses=session_var_value)

# @app.route("/silver", methods=["GET"])
# def silver(): 
#     session_var_value = session.get('key')
#     return render_template('silver.html', title='Silver', ses=session_var_value)


if __name__ == '___main__':
    app.run(debug=True)


@app.route("/callback", methods=["GET"])
def callback():

    try:
        fidor = OAuth2Session(state=session['oauth_state'])

        authorizationCode = request.args.get('code')
        body = 'grant_type="authorization_code&code='+authorizationCode + \
            '&redirect_uri='+redirect_uri+'&client_id=' + client_id
        auth = HTTPBasicAuth(client_id, client_secret)
        token = fidor.fetch_token(token_url, auth=auth,
                                  code=authorizationCode, body=body, method='POST')

        session['oauth_token'] = token
        
        return redirect(url_for('.services'))

        session['key'] = 'loggedin'

        return redirect(url_for('.profile'))

    except:
        print('Error Occured')
        return redirect(url_for('.homepage'))

# @app.route("/gold", methods=["GET"])
# def gold(): 
#     session_var_value = session.get('key')
#     return render_template('gold.html', title='Gold', ses=session_var_value)

# @app.route("/silver", methods=["GET"])
# def silver(): 
#     session_var_value = session.get('key')
#     return render_template('silver.html', title='Silver', ses=session_var_value)

if __name__ == '___main__': 
    app.run(debug=True)

# bitcoin section
@app.route('/bitcoin', methods=['GET'])
def bitcoin():

    session_var_value = session.get('key')

    return render_template('bitcoin.html', title='Bitcoin', ses=session_var_value)


@app.route('/bitcoinresult', methods=['GET', 'POST'])
def bitcoinresult():
    error = None
    if request.method == "POST":
        bitcoinCode = request.form['bitcoinSymbol']
        api_key = 'Y0N5J0ZJLKJACDU2'

        url = "https://www.alphavantage.co/query"

        querystring = {"function": "CURRENCY_EXCHANGE_RATE",
                       "from_currency": "BTC", "to_currency": "SGD", "apikey": api_key}

        headers = {
            'User-Agent': "PostmanRuntime/7.20.1",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "80da5e82-2870-483c-808e-fadd5e500863,12e05540-db9d-4a5f-bed7-f6cbbaacf1e5",
            'Host': "www.alphavantage.co",
            'Accept-Encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }

        response = requests.request(
            "GET", url, headers=headers, params=querystring)

        bitcoinData = json.loads(response.text)

        fromBitcoinCode = bitcoinData["Realtime Currency Exchange Rate"]["1. From_Currency Code"]

        fromBitcoinName = bitcoinData["Realtime Currency Exchange Rate"]["2. From_Currency Name"]

        toBitcoinCode = bitcoinData["Realtime Currency Exchange Rate"]["3. To_Currency Code"]

        toBitcoinName = bitcoinData["Realtime Currency Exchange Rate"]["4. To_Currency Name"]

        lastRefreshedBitcoinDate = bitcoinData["Realtime Currency Exchange Rate"]["6. Last Refreshed"]

        latestExchangeBitcoinRate = bitcoinData["Realtime Currency Exchange Rate"]["5. Exchange Rate"]

    return render_template('bitcoin_rate.html', title='Bitcoin Rate', bFromCode=fromBitcoinCode, bFromName=fromBitcoinName, bToCode=toBitcoinCode, bToName=toBitcoinName, bCode=bitcoinCode, bRate=latestExchangeBitcoinRate, bTime=lastRefreshedBitcoinDate)

#----------------- DBS ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————
@app.route('/DBS', methods=['GET', 'POST'])
def DBS():
    error = None
    api_key = '7Y1YUNF6P6UQA11Q'
    url = "https://www.alphavantage.co/query"
    querystring = {"function": "TIME_SERIES_INTRADAY","symbol": "D05.SI", "interval": "5min", "apikey": api_key}

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

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    DBSData = json.loads(response.text)
    lastRefreshedDate = DBSData["Meta Data"]["3. Last Refreshed"]
    latestStockPrices = DBSData["Time Series (5min)"][lastRefreshedDate]
    DBSCode = 'D05.SI'
    closingPrice = latestStockPrices["4. close"]
    volume = latestStockPrices["5. volume"]

    return render_template('DBS.html', title='DBS Price', bCode=DBSCode, bPrice=closingPrice, bVolume=volume, bTime=lastRefreshedDate)

#----------------- UOB ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————

@app.route('/UOB', methods=['GET', 'POST'])
def UOB():
    error = None
    api_key = '7Y1YUNF6P6UQA11Q'
    url = "https://www.alphavantage.co/query"
    querystring = {"function": "TIME_SERIES_INTRADAY","symbol": "U11.SI", "interval": "5min", "apikey": api_key}

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

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    DBSData = json.loads(response.text)
    lastRefreshedDate = DBSData["Meta Data"]["3. Last Refreshed"]
    latestStockPrices = DBSData["Time Series (5min)"][lastRefreshedDate]
    UOBCode = 'U11.SI'
    closingPrice = latestStockPrices["4. close"]
    volume = latestStockPrices["5. volume"]

    return render_template('UOB.html', title='UOB Price', bCode=UOBCode, bPrice=closingPrice, bVolume=volume, bTime=lastRefreshedDate)

#----------------- OCBC ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————

@app.route('/OCBC', methods=['GET', 'POST'])
def OCBC():
    error = None
    api_key = '7Y1YUNF6P6UQA11Q'
    url = "https://www.alphavantage.co/query"
    querystring = {"function": "TIME_SERIES_INTRADAY","symbol": "O39.SI", "interval": "5min", "apikey": api_key}

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

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    DBSData = json.loads(response.text)
    lastRefreshedDate = DBSData["Meta Data"]["3. Last Refreshed"]
    latestStockPrices = DBSData["Time Series (5min)"][lastRefreshedDate]
    OCBCCode = 'O39.SI'
    closingPrice = latestStockPrices["4. close"]
    volume = latestStockPrices["5. volume"]

    return render_template('OCBC.html', title='OCBC Price', bCode=OCBCCode, bPrice=closingPrice, bVolume=volume, bTime=lastRefreshedDate)


@app.route('/bitcoinnews', methods=['GET'])
def bitcoinnews():
    session_var_value = session.get('key')
    top_headlines = newsapi.get_everything(
        q='bitcoin', language='en', page_size=15)
    news = top_headlines['articles']
    return render_template('bitcoinnews.html', title='Bitcoin News', ses=session_var_value, news=news)


@app.route('/litecoinnews', methods=['GET'])
def litecoinnews():
    session_var_value = session.get('key')
    top_headlines = newsapi.get_everything(
        q='litecoin', language='en', page_size=15)
    news = top_headlines['articles']
    return render_template('litecoinnews.html', title='Litecoin News', ses=session_var_value, news=news)


@app.route('/ethereumnews', methods=['GET'])
def ethereumnews():
    session_var_value = session.get('key')
    top_headlines = newsapi.get_everything(
        q='ethereum', language='en', page_size=15)
    news = top_headlines['articles']
    return render_template('ethereumnews.html', title='Ethereum News', ses=session_var_value, news=news)


@app.route('/equitiesnews', methods=['GET'])
def equitiesnews():
    session_var_value = session.get('key')
    top_headlines = newsapi.get_everything(
        q='equities', language='en', page_size=15)
    news = top_headlines['articles']
    return render_template('equitiesnews.html', title='Equities News', ses=session_var_value, news=news)


@app.route('/forexnews', methods=['GET'])
def forexnews():
    session_var_value = session.get('key')
    top_headlines = newsapi.get_everything(
        q='forex', language='en', page_size=15)
    news = top_headlines['articles']
    return render_template('forexnews.html', title='Forex News', ses=session_var_value, news=news)


@app.route('/currencynews', methods=['GET'])
def currencynews():
    session_var_value = session.get('key')
    top_headlines = newsapi.get_everything(
        q='currency', language='en', page_size=15)
    news = top_headlines['articles']
    return render_template('currencynews.html', title='Currency News', ses=session_var_value, news=news)


@app.route('/metalnews', methods=['GET'])
def metalnews():
    session_var_value = session.get('key')
    top_headlines = newsapi.get_everything(
        q='metals', language='en', page_size=15)
    news = top_headlines['articles']
    return render_template('metalnews.html', title='Metals News', ses=session_var_value, news=news)


@app.route('/oilnews', methods=['GET'])
def oilnews():
    session_var_value = session.get('key')
    top_headlines = newsapi.get_everything(
        q='crude-oil', language='en', page_size=15)
    news = top_headlines['articles']
    return render_template('oilnews.html', title='Oil News', ses=session_var_value, news=news)

# litecoin section
@app.route('/litecoin', methods=['GET'])
def litecoin():
    session_var_value = session.get('key')
    return render_template('litecoin.html', title='Litecoin', ses=session_var_value)


@app.route('/litecoinresult', methods=['GET', 'POST'])
def litecoinresult():
    error = None
    if request.method == "POST":
        litecoinCode = request.form['litecoinSymbol']
        api_key = 'Y0N5J0ZJLKJACDU2'

        url = "https://www.alphavantage.co/query"

        querystring = {"function": "CURRENCY_EXCHANGE_RATE",
                       "from_currency": "LTC", "to_currency": "SGD", "apikey": api_key}

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

        response = requests.request(
            "GET", url, headers=headers, params=querystring)

        litecoinData = json.loads(response.text)

        fromLitecoinCode = litecoinData["Realtime Currency Exchange Rate"]["1. From_Currency Code"]

        fromLitecoinName = litecoinData["Realtime Currency Exchange Rate"]["2. From_Currency Name"]

        toLitecoinCode = litecoinData["Realtime Currency Exchange Rate"]["3. To_Currency Code"]

        toLitecoinName = litecoinData["Realtime Currency Exchange Rate"]["4. To_Currency Name"]

        lastRefreshedLitecoinDate = litecoinData["Realtime Currency Exchange Rate"]["6. Last Refreshed"]

        latestExchangeLitecoinRate = litecoinData["Realtime Currency Exchange Rate"]["5. Exchange Rate"]

    return render_template('litecoin_rate.html', title='Litecoin Rate', lFromCode=fromLitecoinCode, lFromName=fromLitecoinName, lToCode=toLitecoinCode, lToName=toLitecoinName, lCode=litecoinCode, lRate=latestExchangeLitecoinRate, lTime=lastRefreshedLitecoinDate)


# Ethereum section
@app.route('/ethereum', methods=['GET'])
def ethereum():
    session_var_value = session.get('key')
    return render_template('ethereum.html', title='Ethereum', ses=session_var_value)


@app.route('/ethereumresult', methods=['GET', 'POST'])
def ethereumresult():
    error = None
    if request.method == "POST":
        ethereumCode = request.form['ethereumSymbol']
        api_key = 'Y0N5J0ZJLKJACDU2'

        url = "https://www.alphavantage.co/query"

        querystring = {"function": "CURRENCY_EXCHANGE_RATE",
                       "from_currency": "ETH", "to_currency": "SGD", "apikey": api_key}

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

        response = requests.request(
            "GET", url, headers=headers, params=querystring)

        ethereumData = json.loads(response.text)

        fromEthereumCode = ethereumData["Realtime Currency Exchange Rate"]["1. From_Currency Code"]

        fromEthereumName = ethereumData["Realtime Currency Exchange Rate"]["2. From_Currency Name"]

        toEthereumCode = ethereumData["Realtime Currency Exchange Rate"]["3. To_Currency Code"]

        toEthereumName = ethereumData["Realtime Currency Exchange Rate"]["4. To_Currency Name"]

        lastRefreshedEthereumDate = ethereumData["Realtime Currency Exchange Rate"]["6. Last Refreshed"]

        latestExchangeEthereumRate = ethereumData["Realtime Currency Exchange Rate"]["5. Exchange Rate"]

    return render_template('ethereum_rate.html', title='Ethereum Rate', eFromCode=fromEthereumCode, eFromName=fromEthereumName, eToCode=toEthereumCode, eToName=toEthereumName, eCode=ethereumCode, eRate=latestExchangeEthereumRate, eTime=lastRefreshedEthereumDate)


@app.route("/login", methods=['GET', 'POST'])
def login():

    print('login')
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'jscott_p0101@email.com' and form.password.data == 'jscott_p0101':
            flash('You have been logged in!', 'success')

            fidor = OAuth2Session(client_id, redirect_uri=redirect_uri)
            authorization_url, state = fidor.authorization_url(
                authorization_base_url)
            session['oauth_state'] = state
            print("authorization URL is =" + authorization_url)
            return redirect(authorization_url, url_for('.profile'))
        else:
            flash('Invalid username/password. Please try again.', 'danger')
    return render_template('login.html', form=form, title='Login')


@app.route("/profile", methods=["GET"])
def profile():
    session_var_value = session.get('key')
    ple = session.get('oauth_token')

    try:
        # get token
        token = session['oauth_token']
        # get accounts details url
        url = "https://api.tp.sandbox.fidor.com/accounts"
        urlTransfer = "https://api.tp.sandbox.fidor.com/transactions"
        url2 = "https://api.tp.sandbox.fidor.com/internal_transfers"
        
        payload = ""
        headers = {
            'Accept': "application/vnd.fidor.de;version=1;text/json",
            'Authorization': "Bearer "+token["access_token"],
            'Cache-Control': "no-cache",
            'Postman-Token': "ec268b59-71ee-4ffd-9c3d-886b7a8aa7fa,b874d931-d9de-46fa-ac94-e658d726549b",
        }

        # accounts details response
        response = requests.request("GET", url, data=payload, headers=headers)
        response1 = requests.request("GET", urlTransfer, data=payload, headers=headers)
        response2 = requests.request("GET", url2, data=payload, headers=headers)

        # if (trans == trans):
        #     print(trans)

        # print(top_headlines)
        # your current token
        print(token)

        # transfer history response
        receivedHistory = json.loads(response2.text)
        reiHis = receivedHistory['data']
        

        # internal history response
        transferHistory = json.loads(response1.text)
        transferH = transferHistory['data']
        
        customersAccount = json.loads(response.text)
        customerDetails = customersAccount['data'][0]
        customerInformation = customerDetails['customers'][0]
        session['fidor_customer'] = customersAccount

        return render_template('profile.html', title='My Profile', fId=customerInformation["id"],
                               fFirstName=customerInformation["first_name"],
                               fAccountNo=customerDetails["account_number"], fBalance=(
                                   customerDetails["balance"]),
                               fEmailAccount=customerInformation["email"], ses=session_var_value, posts=transferH
                               , reci=reiHis)

    except KeyError:
        # if token expired...
        flash('Token expired!', 'danger')
        session.pop('key', None)
        session.pop('oauth_token', None)
        session.clear()
        print("Key error in services-to return back to index")
        return redirect(url_for('login'))


@app.route('/logout')
def logout():

    # Clear all token and key session
    session.pop('key', None)
    session.pop('oauth_token', None)
    session.clear()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('homepage'))


#crudeoil section
@app.route('/crudeoil_rate', methods=["GET", "POST"])
def crudeoilrate():
    error = None

    # session_var_value = session.get('key')
    # return render_template('crudeoilrate.html', title='Crude Oil Rate', ses=session_var_value)

    url1 = "https://www.quandl.com/api/v3/datasets/OPEC/ORB.json"

    querystring1 = {"api_key":"Y5E16RZGMzxsnwQCckVY", "start_date":"2019-11-30"}

#payload = "{\n\t\"account_id\":\"\",\n\t\"receiver\": \"\",\n\t\"external_uid\": \"\",\n\t\"amount\":\"\",\n\t\"subject\": \"\"\n}"
    headers1 = {
        'Accept': "*/*",
        #'Authorization': "Bearer 0a3dea4272b8be7193d961fb0b304927,Bearer 0a3dea4272b8be7193d961fb0b304927",
        'User-Agent': "PostmanRuntime/7.20.1",
        'Cache-Control': "no-cache",
        'Postman-Token': "db98c1be-8300-4b3f-a259-f0ef3313eb4f,1f451134-3c43-4b37-b497-d3fb0ea5e701",
        'Host': "www.quandl.com",
        'Accept-Encoding': "gzip, deflate",
        #'Content-Length': "88",
        'Cookie': "__cfduid=dc84d28528ac00ee6ee4484085a0ba46c1571886503",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response1 = requests.request("GET", url1, headers=headers1, params=querystring1)

    crudeoil = json.loads(response1.text)
    table1 = crudeoil["dataset"]
    tr = table1["data"][0]
    tr1 = tr.pop(0)
    tr2 = tr.pop(0)
    #Converts data from USD to SGD
    newval = float(tr2)

    nameCrudeOil = crudeoil["dataset"]["name"]
    descCrudeOil = crudeoil["dataset"]["description"]
    lastrefCrudeOil = crudeoil["dataset"]["newest_available_date"]


    api_key2 = 'DOJSMQ3ZWF2XI4O2'

    url2 = "https://www.alphavantage.co/query"   

    querystring2 = {"function":"CURRENCY_EXCHANGE_RATE","from_currency":"USD","to_currency":"SGD","apikey":api_key2}   

    headers2 = {
        'User-Agent': "PostmanRuntime/7.20.1",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "f685f542-2182-4a34-8565-645790857291,006c6402-15c2-4bc7-92f8-5bd2aeed2895",
        'Host': "www.alphavantage.co",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }  

    response2 = requests.request("GET", url2, headers=headers2, params=querystring2)

    conversion = json.loads(response2.text)
    print(conversion)
    convert = conversion["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    date = conversion["Realtime Currency Exchange Rate"]["6. Last Refreshed"]
    convert2 = float(convert)
    conversionrate = convert2 * newval

    return render_template('crudeoil_rate.html', title='Crude Oil Rate', table=tr1, table1=newval, name=nameCrudeOil, desc=descCrudeOil, lastref=lastrefCrudeOil,
                             covert=convert, date=date, cCode=conversionrate)



#gold section
@app.route('/gold', methods=['GET'])
def gold():
    error = None

    url = "https://www.quandl.com/api/v3/datasets/LBMA/GOLD.json"

    querystring = {"api_key":"dtdMAt4GywqNa19PJiR6"}

    headers = {
        'User-Agent': "PostmanRuntime/7.18.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "1bd63ecd-89ed-4e17-a833-a9682a75597d,6a1047bb-f1d1-41fd-b97c-78b28c947cbd",
        'Host': "www.quandl.com",
        'Accept-Encoding': "gzip, deflate",
        'Cookie': "__cfduid=dc38cef7ba8473abba1fc55e60eeffe351571885997",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    gold = json.loads(response.text)
    table = gold["dataset"]["data"][0]

    date = table[0]
    usdam = table[1]
    usdpm = table[2]
    gbpam = table[3]
    gbppm = table[4]
    euroam = table[5]
    europm = table[6]
    # tData = {'date'=date, 'usdam'=usdam, 'usdpm'=usdpm, 'gbpam'=gbpam, 'gbppm'=gbppm, 'euroam'=euroam, 'europm'=europm }

    return render_template('gold.html', title='gold', date=date, usdam=usdam, usdpm=usdpm, gbpam=gbpam, gbppm=gbppm, euroam=euroam, europm=europm)

#silver section
@app.route('/silver', methods=['GET'])
def silver():
    error = None

    url = "https://www.quandl.com/api/v3/datasets/LBMA/SILVER.json"

    querystring = {"api_key":"dtdMAt4GywqNa19PJiR6"}

    headers = {
        'User-Agent': "PostmanRuntime/7.18.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "314692fe-37c7-41c9-9571-fafded1e3c62,802c7215-5930-4788-83e3-af33e0f0607c",
        'Host': "www.quandl.com",
        'Accept-Encoding': "gzip, deflate",
        'Cookie': "__cfduid=dc38cef7ba8473abba1fc55e60eeffe351571885997",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    silver = json.loads(response.text)
    table = silver["dataset"]["data"][0]

    date=table[0]
    usd=table[1]
    gbp=table[2]
    euro=table[3]

    return render_template('silver.html', date=date, usd=usd, gbp=gbp, euro=euro, title='Silver')


    # print(response.text)

@app.route('/index', methods=["GET"])
def default():

    # step 1: user application authorization
    # sending authorization client ID and client Secret to Fidor for authorization
    fidor = OAuth2Session(client_id, redirect_uri=redirect_uri)
    authorization_url, state = fidor.authorization_url(authorization_base_url)
    # state is used to prevent CSRF, keep this for later.
    session['oauth_state'] = state
    print("authorization URL is = " + authorization_url)
    return redirect(authorization_url)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@app.route("/services", methods=["GET"])
def services():
    # fetching a protected resource using an OAuth 2 token.
    try:
        token = session['oauth_token']
        url = "https://api.tp.sandbox.fidor.com/accounts"

        payload = ""
        headers = {
            'Accept': "application/vnd.fidor.de;version=1;text/json",
            'Authorization': "Bearer "+token["access_token"],
            'Cache-Control': "no-cache",
            'Postman-Token': "1ec96583-e911-46b1-8004-68a6b4d2013c,993ea015-3e23-42cd-8185-3b6629a0889d",
        }

        response = requests.request("GET", url, data=payload, headers=headers)
        print("services= " + response.text)
        customersAccount = json.loads(response.text)
        customerDetails = customersAccount['data'][0]
        customerInformation = customerDetails['customers'][0]
        session['fidor_customer'] = customersAccount

        return render_template('services.html', title='Payment Menu', fID=customerInformation["id"],
                               fFirstName=customerInformation["first_name"], fLastName=customerInformation["last_name"],
                               fAccountNo=customerDetails["account_number"], fBalance=(customerDetails["balance"]/100))

    except KeyError:
        print("Key error in services-to return back to index")
        return redirect(url_for('default'))

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@app.route("/bank_transfer", methods=["GET"])
def transfer():
    try:
        customersAccount = session['fidor_customer']
        customerDetails= customersAccount['data'][0]

        return render_template('internal_transfer.html', fFIDORID=customerDetails["id"],fAccountNo=customerDetails["account_number"], fBalance=(customerDetails["balance"]/100))

    except KeyError:
        print("Key error in bank_transfer-to return back to index")
        return redirect(url_for('.index'))

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@app.route("/process", methods=["POST"])
def process():

    if request.method == "POST":
        token = session ['oauth_token']
        customersAccount = session['fidor_customer']
        customerDetails = customersAccount['data'][0]

        fidorID = customerDetails['id']
        custEmail = request.form['customerEmailAdd']
        transferAmt = int(float(request.form['transferAmount'])*100)
        transferRemarks = request.form['transferRemarks']
        transactionID = request.form['transactionID']

        url = "https://api.tp.sandbox.fidor.com/internal_transfers"

        payload = "{\n\t\"account_id\": \""+fidorID+"\", \n\t\"receiver\": \""+ custEmail+"\", \n\t\"external_uid\": \""+transactionID+"\", \n\t\"amount\": "+ str(transferAmt)+",\n\t\"subject\": \""+transferRemarks+"\"\n}\n"
        
        headers = {
            'Accept': "application/vnd.fidor.de;version=1;text/json",
            'Authorization': "Bearer "+token["access_token"],
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
            'Postman-Token': "ce7b9b33-11d5-42e8-ac3f-565035973416,d2836e54-dcb3-41dd-8a12-fb9c8857de5b"
            }

        response = requests.request("POST", url, data=payload, headers=headers)

        print("process="+response.text)

        transactionDetails = json.loads(response.text)
        return render_template('transfer_result.html', fTransactionID=transactionDetails["id"], custEmail=transactionDetails["receiver"], fRemarks=transactionDetails["subject"], famount=(float(transactionDetails["amount"])/100), fRecipientName=transactionDetails["recipient_name"])

