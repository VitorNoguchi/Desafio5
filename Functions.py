#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MongoDB as db
import random
import threading
import logging

func_logger = logging.getLogger(__name__)
func_logger.setLevel(logging.INFO)
func_formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
funcfile_handler = logging.FileHandler('Mastermind.log')
funcfile_handler.setFormatter(func_formatter)
func_logger.addHandler(funcfile_handler)

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
            sample1 = {'Name': usr, 'Target': target_number, 'Count': attempt, 'Result': '', 'past_attempt': []}
            db.DB().insertion_mongo(self.conn.album, sample1)
            func_logger.info('{one},{two},{three}'.format(one='Start', two=usr, three=target_number))
            return 'Bom Jogo'
        else:
            return 'Usuario Ja Existente'

    def tentativa(self, attempt_number, usr):
        try:
            data = self.conn.find_mongo(self.conn.album, usr)
            target_number = data['Target']
            attempt = data['Count']
            id = data['_id']
            list = data['past_attempt']
        except:
            func_logger.exception('Usuario invalido')
        if len(str(attempt_number)) == 4:
            if int(attempt) <= 10:
                list.append(attempt_number)
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
                    func_logger.info('{one},{two},{three},Vitoria,{four}'
                                     .format(one = id, two = usr, three = target_number, four = list))
                    mastermind.remove(self, usr)
                elif result != '1111' and attempt == 10:
                    result = 'GAME OVER'
                    func_logger.info('{one},{two},{three},GAMEOVER,{four}'
                                     .format(one=id, two=usr, three=target_number, four=list))
                    mastermind.remove(self, usr)
                else:
                    func_logger.info('{one},{two},{three},Jogando,{four}'
                                     .format(one=id, two=usr, three=target_number, four=list))
        else:
            result = 'Numero invalido'
            func_logger.error('Numero Invalido')
        updateprocess = threading.Thread(target=self.conn.update, args=[self.conn.album, usr,
                                        target_number, attempt, result, list])
        updateprocess.start()
        return str('{one}    ----    {two} tentativas'.format(one = result, two =attempt))

    def remove(self, usr):
        self.conn.remove(self.conn.album, usr)
        print(self.conn.find_mongo(self.conn.album, usr))

if __name__ == '__main__':
    jogo = mastermind()
    print(jogo.Create_Number())
    print(jogo.Start())
    print(jogo.tentativa(4125))
