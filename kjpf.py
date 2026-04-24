#!/usr/local/bin/python3      #     ----------- kjpf.py  4/15/2026  ---------

from flask import Flask, render_template, request, jsonify, redirect
import os

### ------- ADDED FOR CORS: ----------
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.after_request
def handle_options(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, X-Requested-With"
    return response
### ------- END ADDED FOR CORS -------

HOST = os.popen("hostname").read().strip()
if HOST.lower().startswith('himac'):
    IP = os.popen("ipconfig getifaddr en1" ).read().strip()
else:
    IP = os.popen("hostname -I").read().strip()
PORT = 8090

from kframes import *
iframesrc = "https://bxharold.github.io/pigsfly/"  if HOST.lower().startswith('himac') else "static/jeanpaulVlizard-672x380.jpg"
V_frame = V_frame.format(iframesrc=iframesrc)    # late eval

@app.route('/')
@app.route('/<p>')
def index(p=""):
    param = 'Friend' if p=="" else p
    return render_template('kjpf.html', param=param, M_frame=M_frame, C_frame=C_frame, A_frame=A_frame, B_frame=B_frame, V_frame=V_frame, IP=IP, PORT=PORT)

if __name__ == '__main__':
    # not ready for this yet  camstream = Camstream()
    app.run(host="0.0.0.0", port=f"{PORT}", debug=True)

