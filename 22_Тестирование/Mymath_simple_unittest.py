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

from Mymath_simple import *

class TestAll(unittest.TestCase):

    def test_f(self):
        self.assertEqual(f(5), 10)

    def test_g(self):
        self.assertAlmostEqual(g(5), 11)
01.58
unittest.main()