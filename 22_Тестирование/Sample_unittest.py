#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     19.10.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import unittest


class TestStringMethod(unittest.TestCase):

    def setUp(self):
        """
            Функция выполняется перед каждым тестом
            Метод используется для инициализации ресурсов,
            например открытие файла, подключение к базе данных и т.д.
        """
        self.x = 5

    def tearDown(self):
        """
            Функция выполняется после каждого теста.
            Метод используется для освобождения ранее открытых ресурсов,
            например закрытие файла, отключение от базы данных и т.д.
        """

    def test_upper(self):
        #Убедится, что равны
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'Hello world'
        self.assertEqual(s.split(), ['Hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)
            #s.split('2')#AssertionError: TypeError not raised

    def test_a(self):
        print("Ok!")
        self.assertEqual(self.x, 5)
        self.x = 6

    def test_b(self):
        self.assertEqual(self.x, 5)
        #print(2/0)



if __name__ == '__main__':
#    main()
    unittest.main()
