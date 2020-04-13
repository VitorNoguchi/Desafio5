#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MongoDB as db
import random
import threading

class mastermind:
    def __init__(self):
        self.conn = db.DB()
        self.conn.start_conn('Name', 'Target')

    def Create_Number(self):
        digits = random.sample(range(0, 9), 4)
        number = ''.join(map(str, digits))
        return number

    def Start(self, usr):
        target_number = str(mastermind.Create_Number(self))
        attempt = int(0)
        check = self.conn.check(self.conn.album, usr)
        if check == 'OK':
            sample1 = {'Name': usr, 'Target': target_number, 'Count': attempt, 'Result': ''}
            db.DB().insertion_mongo(self.conn.album, sample1)
            return 'Bom Jogo'
        else:
            return 'Usuario Ja Existente'

    def tentativa(self, attempt_number, usr):
        data = self.conn.find_mongo(self.conn.album, usr)
        target_number = data['Target']
        attempt = data['Count']
        if len(str(attempt_number)) == 4:
            if int(attempt) <= 10:
                attempt_number = str(attempt_number)
                result = ''
                for cont,val in enumerate(target_number):
                    if val in attempt_number and val != attempt_number[cont]:
                        result += str(0)
                    elif val in attempt_number and val == attempt_number[cont]:
                        result += str(1)
                    else:
                        pass
                attempt += 1
                if result == '1111':
                    result = "VOCE VENCEU!"
                    mastermind.remove(self, usr)
                elif result != '1111' and attempt == 10:
                    result = 'GAME OVER'
                    mastermind.remove(self, usr)
                else:
                    pass
        else:
            result = 'Numero invalido'
        updateprocess = threading.Thread(target=self.conn.update, args=[self.conn.album, usr, target_number, attempt, result])
        updateprocess.start()
        return str('{one}    ----    {two} tentativas'.format(one = result, two =attempt))

    def remove(self, usr):
        self.conn.remove(self.conn.album, usr)
        self.conn.find_mongo(self.conn.album, usr)

if __name__ == '__main__':
    jogo = mastermind()
    print(jogo.Create_Number())
    print(jogo.Start())
    print(jogo.tentativa(4125))
