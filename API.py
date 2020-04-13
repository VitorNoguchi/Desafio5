#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from Functions import mastermind

game = mastermind()
app = Flask(__name__)

@app.route('/gera_numero', methods=['GET'])
def foo():
    value = game.Create_Number()
    return jsonify(value)

@app.route('/inicia', methods=['GET'])
def foo1():
    usr = request.args['Name']
    init = game.Start(usr)
    return jsonify(init)

@app.route('/tentativa/<name>/<attempt_number>', methods=['GET'])
def foo2(name = None, attempt_number=None):
    outcome = game.tentativa(attempt_number, name)
    return jsonify(outcome)

@app.route('/deleta', methods = ['GET'])
def foo3():
    usr = request.args['Name']
    game.remove(usr)
    return jsonify('OK')

if __name__ == '__main__':
    app.run(debug=True, port=9999)