#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import MongoClient

class DB:
    def __init__(self):
        self.cliente = ''
        self.banco = ''
        self.album = ''

    def start_conn(self, base, collection):
        self.cliente = MongoClient('mongodb://localhost:27017/')
        self.banco = self.cliente[base]
        self.album = self.banco[collection]

    def insertion_mongo(self, collection, sample):
        collection.insert_one(sample)

    def find_mongo(self, collection, name):
        data = collection.find({'Name': name})
        for a in data:
            return a

    def check(self, collection, name):
        status = 'OK'
        check = collection.find()
        for a in check:
            if a['Name'] == name:
                status = 'NOK'
        return status

    def remove(self, collection, usr):
        collection.remove({'Name': usr})

    def update(self, collection, name, target_number, attempt, result, attempt_list):
        collection.update({'Name': name}, {'Name': name, 'Target': target_number, 'Count': attempt,
                                           'Result': result, 'past_attempt': attempt_list})

if __name__ == "__main__":
    conn = DB()
    conn.start_conn('Name', 'Target')
    teste = DB().find_mongo(conn.album, 'Vitor')
    DB().remove(conn.album, 'Vitor')
    print(teste)
    print(conn.album.count_documents({}))
