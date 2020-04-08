#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

'''
r = requests.get('http://127.0.0.1:9999/gera_numero')
print(r.text)
print(r.status_code)
print(r.content)
print(r.json())
'''

r = requests.get('http://127.0.0.1:9999/inicia')
print(r.text)
print(r.status_code)
print(r.content)
print(r.json())

'''
r = requests.get('http://127.0.0.1:9999/tentativa', params={'novo_valor': 4231})
print(r.text)
print(r.status_code)
print(r.content)
print(r.json())
'''