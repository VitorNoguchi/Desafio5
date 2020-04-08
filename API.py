#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
import random
import threading

app = Flask(__name__)

def gera_numero():
    lista =  []
    while len(lista) < 4:
        x = random.randint(0,9)
        if x not in lista:
            lista.append(x)
            if lista[0] == 0:
                lista.pop(0)
        else:
            pass
    numero = lista[0]*10**3 + lista[1]*10**2 + lista[2]*10**1 + lista[3]
    return numero

def inicia():
    num = str(gera_numero())
    with open('numero.txt', 'w') as f:
        f.write(num)
        f.close()

def tentativa(segundo_numero):
    primeiro_numero = str(gera_numero())
    segundo_numero = str(segundo_numero)
    resposta = ''
    for cont,val in enumerate(primeiro_numero):
        if val in segundo_numero and val != segundo_numero[cont]:
            resposta += str(0)
        elif  val in segundo_numero and val == segundo_numero[cont]:
            resposta += str(1)
        else:
            pass
    return [resposta, primeiro_numero]

@app.route('/gera_numero', methods=['GET'])
def foo():
    valor = gera_numero()
    return jsonify(numero = valor)

@app.route('/inicia', methods=['GET'])
def foo1():
    t = threading.Thread(target=inicia)
    t.start()
    return jsonify(status = 'OK')

@app.route('/tentativa', methods=['GET'])
def foo2():
    segundo_numero = request.args['novo_valor']
    a = tentativa(segundo_numero)
    return jsonify(status = a)


if __name__ == '__main__':
    app.run(debug=True, port=9999)