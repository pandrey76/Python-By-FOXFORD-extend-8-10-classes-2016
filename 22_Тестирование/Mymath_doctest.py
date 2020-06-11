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

#Оформление тестов через doctest
#Подобным образом можно и тестировать классы
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
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
