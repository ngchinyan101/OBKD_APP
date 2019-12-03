from flask import Flask, request, redirect, session, url_for, render_template, flash
from requests_oauthlib import OAuth2Session
from forms import RegistrationForm, LoginForm
from requests.auth import HTTPBasicAuth
import requests
import json

app = Flask(__name__)

app.config['SESSION_TYPE']='memcached'
app.config['SECRET_KEY'] = '031e8b93c90984f2c4a8bf0d0b7b3360'

client_id = "8d7f7404c85cca13"
client_secret = "031e8b93c90984f2c4a8bf0d0b7b3360"
authorization_base_url = 'https://apm.tp.sandbox.fidor.com/oauth/authorize'
token_url = 'https://apm.tp.sandbox.fidor.com/oauth/token'
redirect_uri = 'http://localhost:5000/callback'

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
    return render_template('preciousmetal.html', title='Precious Metal',ses=session_var_value)

@app.route("/crudeoil", methods=["GET"])
def crudeoil(): 
    session_var_value = session.get('key')
    return render_template('crudeoil.html', title='Crude Oil', ses=session_var_value)

@app.route("/cryptocurrencyindex", methods=["GET"])
def cryptocurrencyindex(): 
    session_var_value = session.get('key')
    return render_template('cryptocurrencyindex.html', title='Purchase of Cryptocurrency', ses=session_var_value)

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

        session['key'] = 'loggedin'

        return redirect(url_for('.profile'))

    except:
        print('Error Occured')
        return redirect(url_for('.homepage'))

# bitcoin section
@app.route('/bitcoin', methods=['GET'])
def bitcoin():

    session_var_value = session.get('key')

    return render_template('bitcoin.html', title='Bitcoin', ses=session_var_value)

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
    session_var_value = session.get('key')
    return render_template('litecoin.html', title='Litecoin', ses=session_var_value)

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
        

    return render_template('litecoin_rate.html', title='Litecoin Rate', lFromCode=fromLitecoinCode, lFromName=fromLitecoinName, lToCode=toLitecoinCode, lToName=toLitecoinName, lCode=litecoinCode, lRate=latestExchangeLitecoinRate, lTime=lastRefreshedLitecoinDate)

# Ethereum section
@app.route('/ethereum', methods=['GET'])
def ethereum():
    session_var_value = session.get('key')
    return render_template('ethereum.html', title='Ethereum', ses=session_var_value)

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

@app.route("/login", methods=['GET', 'POST'])
def login():
    
    print('login')
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'jscott_p0101@email.com' and form.password.data == 'jscott_p0101':
            flash('You have been logged in!', 'success')

            fidor = OAuth2Session(client_id, redirect_uri=redirect_uri)
            authorization_url, state = fidor.authorization_url(authorization_base_url)
            session['oauth_state'] = state
            print("authorization URL is =" + authorization_url)
            return redirect(authorization_url,url_for('.profile'))
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
        
        payload = ""
        headers = {
            'Accept': "application/vnd.fidor.de;version=1;text/json",
            'Authorization': "Bearer "+token["access_token"],
            'Cache-Control': "no-cache",
            'Postman-Token': "ec268b59-71ee-4ffd-9c3d-886b7a8aa7fa,b874d931-d9de-46fa-ac94-e658d726549b",
        }

        # accounts details response
        response = requests.request("GET", url, data=payload, headers=headers)

        # if (trans == trans): 
        #     print(trans)

        # print(top_headlines)
        # your current token
        print(token)
        
        customersAccount = json.loads(response.text)
        customerDetails = customersAccount['data'][0]
        customerInformation = customerDetails['customers'][0]
        session['fidor_customer'] = customersAccount

        return render_template('profile.html', title='My Profile', fId=customerInformation["id"], 
                               fFirstName=customerInformation["first_name"], 
                               fAccountNo=customerDetails["account_number"], fBalance=(
                                   customerDetails["balance"]),
                               fEmailAccount=customerInformation["email"], ses=session_var_value)

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



@app.route('/crudeoil_rate', methods=["GET", "POST"])
def crudeoilrate():
    error = None

    # session_var_value = session.get('key')
    # return render_template('crudeoilrate.html', title='Crude Oil Rate', ses=session_var_value)

    url = "https://www.quandl.com/api/v3/datasets/OPEC/ORB.json"

    querystring = {"api_key":"Y5E16RZGMzxsnwQCckVY", "start_date":"2019-11-30"}

#payload = "{\n\t\"account_id\":\"\",\n\t\"receiver\": \"\",\n\t\"external_uid\": \"\",\n\t\"amount\":\"\",\n\t\"subject\": \"\"\n}"
    headers = {
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

    response = requests.request("GET", url, headers=headers, params=querystring)

    crudeoil = json.loads(response.text)
    table1 = crudeoil["dataset"]
    tr = table1["data"][0]
    tr1 = tr.pop(0)
    tr2 = tr.pop(0)


    return render_template('crudeoil_rate.html', table=tr1, table1=tr2)

