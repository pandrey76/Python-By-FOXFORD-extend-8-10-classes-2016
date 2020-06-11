#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     18.10.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#   QA - Quality Assurance (отдел тестирования)

#   Runtime error
#   В Python это называется исключения, оторве мы можем перехватывать

#   Exception - Базовый класс исключений.
# Можно писать свои классы наследуемые от Exception.

from os import sys

    #Создаём свою ошибку
class MyError_(Exception):
    pass

class MyError(Exception):
    def __init__(self, lineno, text):
        self.lineno = lineno
        self.text = text
    def __str__(self):
        return "my error" + text + " in line" + str(self.lineno)

def main():
    try:
        print(2 + 2)
    except: #:данная конструкция перехватывает все исключения
        pass
#   С синтаксическими ошибками ничего сделать нельзя

    a = int(input())    #2
    b = int(input())    #0
    try:
        print(a / b)
    except ZeroDivisionError as e:
        print("b = 0!!")    #   b = 0!!
        print(e)    #   division by zero
        #sys.exit()  #даже после этой инструкции блок finally выполнится
    except Exception:   #тоже самое что и "execept:"
        print("Unknow error")
    else:
        print("Ok!")
    finally:    #Выполняется всегда!!
        print("All running!!")  #   All running!!


    user = "aaa"
    if user != "bbb":
        try:
            raise NameError("Wrong User!")
        except:
            print("Ok!")

    if 1 != 2:
#        raise MyError_("message")
        raise MyError(7, "Message")

if __name__ == '__main__':
    main()
