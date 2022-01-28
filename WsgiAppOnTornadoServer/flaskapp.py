#!/usr/bin/env python

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'status': 'ok'})

