from unicodedata import name
from flask import Flask
app = Flask(__name__)

import requests

@app.route('/')
def ping_service():
    return 'Hello, I am ping service!'

@app.route('/ping')
def do_ping():
    ping = 'Ping...'

    responce = ''
    try:
        responce = requests.get('http://pong:5001')
    except requests.exceptions.RequestException as e:
        print('\n Cannot reach the pong service')
        return 'Ping ...\n'

    return 'Ping ...' + responce.text + '\n'

if __name__=='__main__':
    app.run(host = '0.0.0.0', port = 5000, debug = True)
