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
def factorial(n):   # 1 * 2 * 3 * ... * n
    """
        Calculates
        mathematical function n!

        Блок doctest
        (Третий тест неправильный)

        >>> factorial(5)
        120
        >>> factorial(0)
        1
        >>> factorial(6)
        800

    """
    result = 2
    for i in range(1, n + 1):
        result *= i
    return result

def binom(n, k):
    """
    """
    return factorial(n) // (factorial(k) * factorial(n - k))

if __name__ == '__main__':
    print(binom(4, 2))  #   6
