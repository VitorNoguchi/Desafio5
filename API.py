#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
import Functions
import logging

game = Functions.mastermind()
app = Flask(__name__)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('Mastermind.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

@app.route('/gera_numero', methods=['GET'])
def foo():
    try:
        value = game.Create_Number()
        return jsonify(value)
    except:
        logger.exception('Erro Gera Numero')

@app.route('/inicia', methods=['GET'])
def foo1():
    try:
        usr = request.args['Name']
        init = game.Start(usr)
        print('inicia')
    except:
        logger.exception('Necessario 1 Nome')
    return jsonify(init)

@app.route('/tentativa/<name>/<attempt_number>', methods=['GET'])
def foo2(name = None, attempt_number=None):
    try:
        outcome = game.tentativa(attempt_number, name)
    except:
        logger.exception('Inputs invalidos')
    return jsonify(outcome)

@app.route('/deleta', methods = ['GET'])
def foo3():
    usr = request.args['Name']
    game.remove(usr)
    return jsonify('OK')

if __name__ == '__main__':
    app.run(debug=True, port=9999)
