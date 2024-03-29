﻿#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     20.10.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Для серьёзных проектов необходима поддержка "Непрерывной сисемы тестирования"
#(Continuous integration), в частности для того чтобы проверять работу ваших компонент
#под различные платформы (Windows, Linux и Mac и т.д.).
#При этом тесты могут запускаться по какому нибудь событию.

#Такие системы вместе с unittest могут гарантировать, что ваши компоненты работают правильно.
#Правильность работы ваших компонент не гпарантирует правильность работы всего проекта в целом,
#Для этого необходимо вводить интеграционное тестирование, но это уже работа отдела Тестирования.

#Идея такая, что если вы хототе убедится в правильности работы ваших классов, вам
#необходимо "замокать" все методы, написанные не вами, для того чтобы всегда знать
#что именно в ваших компонентах отсутствуют ошибки.

from unittest.mock import *
#Отличия "Mock" от "MagicMock" с помощь "MagicMock" позволяет налету создавать всякие служебные методы.
class ProductionClass:
    def method(self):
        self.something(1, 2, 3)
    def something(self, a, b, c):
        """
            Данный метод пока не написан, но нам
            необходимо проводить тестирвание класса и этой функции в том числе.
        """
        pass

def main():
    real = ProductionClass()
    #Здесь мы определяем что "somthing" - это mock метод
    real.something = MagicMock()
    real.method()
    #Здесь мы проверяем, что в методе "method" единажды вызывется метод
    #"somthing" с параметрами: "1, 2, 3".
    #Другими словами убеждаемся, что метод "sometging', объекта "real", вызывался
    #один раз с параметрами "1, 2, 3".
    real.something.assert_called_onece_whith(1, 2, 3)


    #Есть ещё примеры
    mock = Mock()
    mock.method.return_value = 3
    print(mock.method())        # 3

    #Тоже самое устанавливаем в конструкторе
    mock = Mock(return_value = 3)
    print(mock())   #   3

    #Если необходимы поля, то делаем так
    mock = Mock()
    mock.x = 3
    print(mock.x)   #   3


#Используем "mock" с "unittest"

if __name__ == '__main__':
    main()
