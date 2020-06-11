#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     09.10.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Создаём класс представляющий обыкновенную дробь
#В самом Python ничего подобного нет

#   a/b     1/3 + 1/7 = 10/21

#   Класс должен быть такой (Техническое Задание)
#   -   Конструктор
#   -   +, -
#   -   *, /
#   -   sqr
#   -   sqrt
#   -   числитель, знаменатель
#   -   сокращение
#   -   перевод из/в 10 систему исчисления
#   -   печать (для отладки)
#   -   ==
#   -   <

from functools import total_ordering

@total_ordering
class Frac:
    def __init__(self, numerator, denominator = 1):   #    numerator / denominator
#        if denominator == 0:
#            raise ZeroDivisionError()
        if type(numerator) == int and type(denominator) == int:
            numerator / denominator   #Если b == 0, то будет сгенерировано исключение ZeroDivisionError
            self.numerator = numerator
            self.denominator = denominator
        else:
            raise TypeError()

#Наименьший общий делитель в программировании не имеет никакого смысла, т.к.
#приходится проводить несколько операций деления, которые являются очень дорогими.
#Необходимо привести всё к трём умножениям.

#   8     5     8 * 4 + 5 * 6
#   -  +  -  =  -------------
#   6     4          6 * 4


#-------------------------------------------------------------------------------
#Если мы пишем какую нибудь функцию в классе, которую мы не планируем вызывать снаружи,
# то принято её название начинать с подчёркивания, это означает, что это служебная функция
# (protected функция).
    def _gcd(self):
        """
            НОД - наибольший общий делитель (Greatest Common Deviser)
            Эта функция реализована в библиотеке math.
        """
        #Алгоритм Евклида
        a, b = self.numerator, self.denominator
        while b:
            a, b = b, a % b
        return a
#-------------------------------------------------------------------------------

    def reduce(self):
        """
            Функция сокращения дроби, через нахождение наибольшего общего
            делителя 87/30 ---> 29/10.
        """
        #Алгоритм Евклида
        a, b = self.numerator, self.denominator
        while b:
            a, b = b, a % b
        b = self.denominator // a
        a = self.numerator // a
        return a, b

    def __str1__(self):  # c a/b    2 3/7
        d = self._gcd()
        #Деление с остатком (целочислено)
        a = self.numerator // d
        b = self.numerator // d
        c = a // b
        a = a % b
        if b == 1:
            return str(c)
        else:
            return str(c) + " " + str(a) + "/" + str(b)

    def __str__(self):  # c a/b    2 3/7
        a, b = self.reduce()
        int_part = a // b
        new_num = a % b
        if b == 1:
            return str(int_part)
        else:
            return str(int_part) + " " + str(new_num) + "/" + str(b)

    def __add__(self, other):
        if type(other) == int:
            other = Frac(other, 1)
        return Frac(self.numerator * other.denominator + self.denominator * other.numerator, self.denominator * other.denominator)

    def __radd__(self, other):
        return self + other


    def __eq__(self, other):
        """
            ==
        """
        if type(other) == int:
            other = Frac(other, 1)
        num_1, denum_1  = self.reduce()
        num_2, denum_2  = other.reduce()
        return num_1 == num_2 and denum_1 == denum_2

    def __lt__(self, other):
        """
            <
        """
        #return self.numerator * other.denominator - self.denominator * other.numerator < 0 #При отрицательных числах будет работать не правильно
        num_1, denum_1  = self.reduce()
        num_2, denum_2  = other.reduce()
        return num_1 * denum_2 - num_2 * denum_1 < 0

    def __float__(self):
        """
            Перевод в действительное сичло (десятичную систему).
        """
        return self.numerator / self.denominator

    def __neg__(self):
        return Frac(-self.numerator, self.denominator)


    def __truediv__(self, other):
        return Frac(self.numerator * other.denominator, self.denominator * other.numerator)

def main():
    #Исправить (Frac(1, -6) --->   -1 5/6    --> -1 + 5/6 будет действительно -1/6,
    #но выводится должно сразу -1/6.
    f = Frac(1, 6)
    print(f)

    #Вызываем функцию __add__ класса Frac.
    #Первый объект self, а второй other.
    f1 = Frac(1, 2) + Frac(1, 3)
    print(f1)

    #Операция сравнения: Равно (==)
    f = Frac(1, 2)
    g = Frac(-2, -4)
    print(f == g)   #True


    #Операция сравнения: Меньше (<)
    f = Frac(1, 2)
    g = Frac(-3, -4)
    print(f < g)   #True
    #По умолчанию Python вызовет функцию __eq__ и инвертирует результат
    print(f != g)   #True
    print(f == g)   #False
    print(f >= g)   #False  #Будет работать из-за декоратора @total_ordering
    print(f <= g)   #True  #Будет работать из-за декоратора @total_ordering

    f = Frac(-1, 3)
    g = Frac(2, 3)
    print(f + 2)    #1 2/3
    print(f + g)
    print(2 + f)    #unsupported operand type(s) for +: 'int' and 'Frac'
                    #Генерируется исключение NotImplemented и Python сам пытается вызвать метод __radd__() класса Frac.
                    #После реализации метода __radd__() будет выведено 1 2/3
                    #Аналогичным способом мы можем сделать умножение, вычитание и т.д
                    #кроме опреации деления, она зашита в код Python и ничего сделать нельзя "a = 2 / 3", кроме как явно написать "Frac ( 2, 3)".

    print(float(f + g)) #0.3333333333333333

    print(Frac(1,3) / Frac(2,4))    #   0 2/3


    f = Frac(2)
    print(f)    #   2
    print(type(f))  #<class '__main__.Frac'>

#magic methods в Python

#Посмотреть можно например здесь:
#   www.python-course.eu/python3_magic_methods.php

#Binary Operarors
#-------------------------------------------------------------------------------
#   +           object.__add__(self, other)
#   -           object.__sub__(self, other)
#   *           object.__mul__(self, other)
#   //          object.__floordiv__(self, other)
#   /           object.__div__(self, other)
#   %           object.__mod__(self, other)
#   **          object.__pow__(self, other[,modulo])
#   <<          object.__lshift__(self, other)
#   >>          object.__rshift__(self, other)
#   &           object.__and__(self, other)
#   ^           object.__xor__(self, other)
#   |           object.__or__(self, other)
#-------------------------------------------------------------------------------

#Extended Assigments
#-------------------------------------------------------------------------------

#Автоматически определяются если определены Binary Operators.

#-------------------------------------------------------------------------------

#Unary Operators
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

#Extended Assigments
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

#Comparison Operators
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

#Перед классом можно использовать декоратор @total_ordering  и тогда определив метод __eq__() и  один из методов
#__lt__(), __le__(), __gt__(), __ge__() в классе будут работать все операции сравнения (==, < , > и т.д.)

if __name__ == '__main__':
    main()
