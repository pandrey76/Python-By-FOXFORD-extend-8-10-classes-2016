#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     11.10.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from frac import Frac


def solve_linear_equation(a, b):    #ax + b = 0
    """
        Решение линейного уравнения.
    """
    if a != 0:
        return -b / a
    elif b != 0:
        return "No solution"
    else:
        return "Any number"

def main():
    f = Frac(5,3)   #1 2/3
    print(f)
    print(solve_linear_equation(2, 4))  #   -2.0

    #   Здесь  мы показали, что код  который работал с целыми числами, также легко будет работать с дробями!!!
    print(solve_linear_equation(Frac(1,2), Frac(1,4)))  #   -1 1/2
    print(solve_linear_equation(Frac(0,2), Frac(1,4)))  #   No solution
    print(solve_linear_equation(Frac(0,2), Frac(0,4)))  #   Any number

#-------------------------------------------------------------------------------
    #Две идентичных операции
    print(solve_linear_equation(3, -2))  #   0.6666666666666666
    print(solve_linear_equation(Frac(3, 1), Frac(-2,1)))  #   0 2/3
    print(solve_linear_equation(Frac(3), Frac(-2)))  #   0 2/3
#-------------------------------------------------------------------------------


if __name__ == '__main__':
    main()
