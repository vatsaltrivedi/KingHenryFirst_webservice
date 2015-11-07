from flask import Flask, jsonify
import requests
app = Flask(__name__)


@app.route('/')
def index():
    return 'King Henry First Web Service'

# Get the latest rate: "127.0.0.1/rate" or http://domainname/rate
# similar url for all the methods or services

@app.route("/rate")
def rate():
	return requests.get('https://shapeshift.io/rate/btc_ltc').content

#Get List of Supported Coins with Icon Links
@app.route('/coins')
def coins():
	return requests.get('https://shapeshift.io/getcoins').content

#deposit limit
@app.route('/limit')
def limit():
	return requests.get('https://shapeshift.io/limit/btc_ltc').content

#market Info
@app.route('/marketinfo')
def marketinfo():
    return requests.get('https://shapeshift.io/marketinfo/btc_ltc').content

# Recent Transaction [10]
@app.route('/transaction')
def transaction():
	return requests.get('https://shapeshift.io/recenttx/10').content

#Status of deposit to address
@app.route('/status/<address>')
def status(username):
	return requests.get('https://shapeshift.io/txStat/%s' %address).content

#Time Remaining on Fixed Amount Transaction
@app.route('/timeremaining/<address>')
def time(username):
	return requests.get('https://shapeshift.io/timeremaining/%s' %address).content



if __name__ == '__main__':
    app.run()

