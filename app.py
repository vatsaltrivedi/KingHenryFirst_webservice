from flask import Flask, jsonify
import requests
app = Flask(__name__)


@app.route('/')
def index():
    return 'Flask is running!'


@app.route('/marketinfo')
def names():
    return requests.get('https://shapeshift.io/marketinfo/btc_ltc').content

if __name__ == '__main__':
    app.run()

