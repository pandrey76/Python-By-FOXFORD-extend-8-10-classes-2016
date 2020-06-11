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

            #Решение уравнений с одним неизвестным
            #           Equation    F(x) = 0
#Класс линейных уравнений   Клас квадратных уравнений       Многочлен       Решение уравнений
# LinEquation               SquareEquation                  Polynom         Solution

#Наследование определяется как является, например Мерседес является машиной.

#"Утиная" типизация - всё, что ходит как утка и крякает как утка является уткой.

class Eq_:
    pass

class LinEq_:
    """
        ax + b = 0
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def solve(self):
        if self.a == self.b == 0:
            return "Any number"
        elif self.a == 0:
            return None
        else:
            return -self.b / self.a



class LinEq_P:
    """
        Здесь мы определили связь полинома и линейного уравнения, т.е
        линейное уравнение определяется из полинома
    """

    def __init__(self, poly):
        self.poly = poly

    def solve(self):
        if self.poly[1] == self.poly[0] == 0:
            return "Any number"
        elif self.poly[0] == 0:
            return None
        else:
            return -self.poly[0] / self.poly[1]

class SqEq_P(Eq_):
    def __init__(self, poly):
        self.poly = poly


class Polynom:
    """
        #a0 + a1x + a2x**2 + ...
    """
    def __init__(self, a):
        self.coef = a

    def __str__(self):
        #result = str(self.coef[0]) #Первый вариант
        result = str(self[0])       #Второй вариант
        for i in range(1, len(self.coef)):
            #result += "+" + str(self.coef[i]) + "x**" + str(i) #Первый вариант
            result += "+" + str(self[i]) + "x**" + str(i) #Второй вариант

        return result
#-------------------------------------------------------------------------------
    def __getitem__(self, index):
        """
            Магический метод для индексирования объекта,
            т.е. как обращение к элементам масива.
        """
        return self.coef[index]

    def __setitem__(self, index, value):
        """
            Магический метод для индексирования объекта,
            т.е. как изменения элемента масива.
        """
        self.coef[index] = value
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
    def __call__(self, x):
        """
            Определяем, что объект Polynom является вызываемым
            Например:
                p = Polynom([1, 2, 0, 3, 4])
                print(p(5)) #Вызов метода __call__(self, x):
            В данном конкретном случае вычисление полимома при известном X.
        """
        result = self[0]
        for i in range(1, len(self.coef)):
            result += self[i] * x**i
        return result
#-------------------------------------------------------------------------------


class Eq:
    def __init__(self, f):
        self.f = f

    def solve_int(self):
        result = []
        for i in range(-100000, 100000):
            if self.f(i) == 0:
                result.append(i)
        return result

    def solve(self, rang):
        result = []
        for j in range(-100000, 100000):
            i = j / 1000
            if abs(self.f(i)) < rang:
                result.append(i)
        return result

class PolEq(Eq):
    """
        #a0 + a1x + a2x**2 + ... = 0
    """
    def __init__(self, poly):
        self.poly = poly

    def __str__(self):
        return str(self.poly) + " = 0"

class Sqeq(PolEq):
    pass

class LinEq(PolEq):
    """
    """

    def solve(self):
        if self.poly[1] == self.poly[0] == 0:
            return "Any number"
        elif self.poly[0] == 0:
            return None
        else:
            return -self.poly[0] / self.poly[1]
def main():
    e = LinEq_(4,2)
    print(e.solve())

    p = Polynom([1, 2, 0, 3, 4])    #1+2x**1+0x**2+3x**3+4x**4
    print(p)        #1+2x**1+0x**2+3x**3+4x**4
    print(p.coef[3])    #   3
    print(p[3])    #   3
    p[3] = 1
    print(p[3])    #   1
    p[3] = 3
    print(p[3])    #   3

    print(p(5)) #Если не определить магический метод __call__, то Python выдаст ошибку
                #   'Polynom' object is not callable
                #   2886

    p1 = Polynom([1, 2, 1])    #1+2x**1+1x**2
    print(p1)        #1+2x**1+1x**2
    print(p1(5))     # 36


    p2 = Polynom([1,2])
    e = LinEq_P(p2)
    print(e.solve())    #-0.5

    p = Polynom([1, 2, 3, 4])
    e = PolEq(p)
    print(e)        #   1+2x**1+3x**2+4x**3 = 0

    e = LinEq(p)
    print(e)        #   1+2x**1+3x**2+4x**3 = 0


#   2 /x**2 + 1 - 2 = 0
#Создать уравнение можно двумя способами
#   Первый создать функцию
    def f1(x):
        return 2 / (x**2 + 1) - 2
#   Второй способ с помощью lambda функции
    f2 = lambda x: 2 / (x**2 + 1) - 2
    e = Eq(f1)
    print( e.solve_int())   #   [0]

    f2 = lambda x: 2 * x - 4
    e = Eq(f2)
    print( e.solve_int())   #   [2]

    f2 = lambda x: 2 / (x**2 + 1) - 2
    e = Eq(f2)
    print( e.solve_int())   #   [0]

    f2 = lambda x: 2 / (x**2 + 1) - 1
    e = Eq(f2)
    print( e.solve_int())   #   [-1, 1]

    f2 = lambda x: x**2 - 2
    e = Eq(f2)
    print( e.solve(0.001))   #   [-1.414, 1.414]

    f2 = lambda x: x**3 - 2
    e = Eq(f2)
    print( e.solve(0.001))   #   [1.26]

    f2 = lambda x: x**4 - 2
    e = Eq(f2)
    #Уменьшив точность до 0.01 мы нашли много корней, но если присмотрется то их 3
    print( e.solve(0.01))   #   [-1.19, -1.189, -1.188, 1.188, 1.189, 1.19]

    f2 = lambda x: x**8 - 2
    e = Eq(f2)
    print( e.solve(0.022))   #   [-1.092, -1.091, -1.09, 1.09, 1.091, 1.092]


#    p = Polynom([1, 2, 3, 4, 5])
#    e = PolEq(p)
#    print(e.solve(0.22))

    p = Polynom([2, 1])
    e = LinEq(p)
    print(e.solve())
    print(e.solve_int())

if __name__ == '__main__':
    main()
