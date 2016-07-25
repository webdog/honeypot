#!/usr/bin/env python3
from flask import Flask, request, Response
import os

app = Flask(__name__)


#Get the hooks we want to monitor from the environment variables
def hk_envs():
	vals = {}
	for k, v in os.environ.items():
		if "hk-" in k and  v == "True":
			vals[k] = v
		else:
			pass
	return vals

# Assign to variable so we only call the environment once
hks_true = hk_envs()


@app.route('/')
def hello_world():
	return "Nothing to see here. Move along."

@app.route('/receive', methods = ['POST'])
def process_post():
	headers = request.headers
	resp = Response(status=200, mimetype='application/json')
	for k, v in headers.items():
		if v not in hks_true:
			return resp
		else:
			message = request.to_json()
			return resp
@app.route('/receive', methods = ['GET'])
def receive_get():
	return "Nothing to see here. Move along."

if __name__ == '__main__':
	app.run()


