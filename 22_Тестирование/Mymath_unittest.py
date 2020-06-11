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

from Mymath import *

class TestFactorial(unittest.TestCase):

    def test_ziro(self):
        self.assertEqual(factorial(0), 1)

    def test_noneziro(self):
        self.assertAlmostEqual(factorial(5), 120)
        self.assertAlmostEqual(factorial(1), 1)


class TestBinom(unittest.TestCase):

    def test_all(self):
        self.assertEqual(binom(4, 2), 6)


unittest.main()
