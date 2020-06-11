#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     02.10.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#   Рекоменбуется посмотреть реализацию классов в стандартной библиотеке Python
#   Python\Lib\... (например: tutle.py или fractions.py)


#-------------------------------------------------------------------------------
def f1(x):
    x = x + 1
    print(x)    #2 т.к x ссылается на объект 2

a = 1
f1(a)
print (a)   #1 #Т.к a ссылается на объект 1
#Это свойство неизменяемых объектов, т.е. нельзя внутри функции изменить
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
def f2(x):
    x[1] = 5
    print (x)   #[1, 5, 3] Изменится т.к. это ссылка на масив

a = [1, 2, 3]
f2(a)
print(a)    #[1, 5, 3] И здесь всё изменится т.к. это ссылка на масив

#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
def f3(x):
    x = [2, 3, 4]
    print (x)   #[2, 3, 4] x стал ссылатся на другой масив

a = [1, 2, 3]
f3(a)
print(a)    #[1, 2, 3] а продолжает ссылатся на исходный масив
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
def f4(x):
    print(id(x))    #18216400 изначально id от a и x совпадали
    x = x + 1
    print(id(x))    #14855144 теперь у x другая ссылка
    print (x)   #2 x стал ссылатся на 2

a = 1
print(id(a))    #18216400
f4(a)
print(a)    #1 а продолжает ссылатся на исходное значение
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
def f5(x):
    global a
    a = a + 1
#Но так никто не делает, т.к. ваша функция меняет глобальную переменную
#и вам всегда надо перед использованием функции определить переменную а.
#Если нам надо поменять число, в функции то надо сделать объект или список
#и именно их передавать в функцию.

a = 1
print(id(a))    #18216400
f5(a)
print(a)    #1 а продолжает ссылатся на исходное значение
print(id(a))    #18216400
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#В Python есть ряд встроенных объектов
a = list()  #list можно определить и так a = []. Мы создаём пустой список
a.append(4)
print (a)
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
class VerySampelCar:
    pass
c = VerySampelCar()
d = VerySampelCar()
print(c)    #   <__main__.VerySampelCar object at 0x011CEB30>
print(d)    #   <__main__.VerySampelCar object at 0x0113E9B0>
d = c
print(d,c)  #   <__main__.VerySampelCar object at 0x0113EA50> <__main__.VerySampelCar object at 0x0113EA50>
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#Python позволяет присвоить экземпляру объекта любые поля. В Python не проверяются
#типы, для Python это нормально, что одна и таже переменная по ходу выполнения
#программы может менять свой тип. Основной минус такого подхода заключается в том,
#что в больших проектах по ошибке можете передать в число строку и в момент
#арифмитической операции с этим числом в Runtime получить ошибку и эту ошибку
#будет тяжело отследить. например год Web сервер будет отлично работать, а потом
#обвалится по причине того, что будет выполнен шаг алгоритма, который никогда
#раньшне не выполнялся.
#В Python нет понятия объявить переменную, можно только её (переменной) присвоить значение.
class SampelCar:
    pass
c = SampelCar()
c.color = "red" #   Американский вариант (color)
c.speed = 50

d = SampelCar()
d.colour = "black"  #   Английский вариант (colour)
d.speed = 100
print(c,d)  #   <__main__.SampelCar object at 0x0113E7D0> <__main__.SampelCar object at 0x0113E7F0>
print(c.speed - d.speed)    #   -50
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
class Car_1:
    pass

    def increase_speed(self, delta):
        if self.speed + delta < 200:
            self.speed += delta
        else:
            self.speed = 200

c = Car_1()
c.speed = 50
c.increase_speed(10)
print(c.speed)  #   60
c.increase_speed(100)
print(c.speed)  #   160
c.increase_speed(100)
print(c.speed)  #   200
c.increase_speed(100)
print(c.speed)  #   200
c.increase_speed(100)
print(c.speed)  #   200
c.increase_speed(100)
print(c.speed)  #   200
c.increase_speed(100)
print(c.speed)  #   200

#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
class Car_2:

    def __init__(self):
        self.speed = 0
        self.color = None


    def increase_speed(self, delta):
        if self.speed + delta < 200:
            self.speed += delta
        else:
            self.speed = 200

c = Car_2()   #Это сокращение для вызова двух методов
            #__new__ этот метод определён по умолчанию для всех классов, которые мы создаём
            # и занимается он тем, что выделяет память и создаёт в этой памяти пустой объект.
            #и он возвращает ссылку на этот оюъект, которая в переменную "с" в качестве ссылки и попадает.
            #Другими словами запись "c = Car_()" эквивалентна "c = Car_.__new__()", метод __new__ обычно никто не меняет, т.к.
            #это очень специфично, т.к. врятли кому нибудь понадобится менять способ выделения памяти под объект,
            #а метод __init__ обычно переписывают, потому что по умолчанию он ничего не делает. А делать он должен
            #начальную инициализацию, т.е. присвоение начальных значений.

print(c.speed)  #   0
c.increase_speed(100)
print(c.speed)  #   100

#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
class Car_3:

    def __init__(self, speed, color):
        self.speed = speed
        self.color = color


    def increase_speed(self, delta):
        if self.speed + delta < 200:
            self.speed += delta
        else:
            self.speed = 200

c = Car_3(50, "red")
c.increase_speed(100)
print(c.speed)  #   150

#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
class Car_4:

    def __init__(self, speed = 0, color = None):
        self.speed = speed
        self.color = color


    def increase_speed(self, delta):
        if self.speed + delta < 200:
            self.speed += delta
        else:
            self.speed = 200

c = Car_4(50, "red")
c.increase_speed(100)
print(c.speed, c.color)  #   150 red

d = Car_4()
d.increase_speed(100)
print(d.speed, d.color)  #   100 None

c = Car_4(50, "red")
d = Car_4(100, "blue")
print(c, d)  #   <__main__.Car_4 object at 0x0113ECB0> <__main__.Car_4 object at 0x0113EB10>
             #Информация выведенная через print абсолютно не информативная.

#********************************
print(1)        #   1       str(1)
print("abc")    #   abc     str("abc")
print(1 >1)     #   False   str(1 > 1)
print(c)        #   <__main__.Car_4 object at 0x0113E970>   str(c)
#Функция print у всех объектов переданных ей вызывает метод "str"
#********************************

#В Python есть методы, которые называются "magic methods", они обычно обрамлены двумя подчёркиваниями спереди и сзади.
#например: __add__
#Почему они magic, потому что в явном виде их никто не вызывает, обычно их вызывают в другом виде.
# 2 + 3 можно записать в виде 2.__add__(3).
#У любого объекта есть метод __str__, который косвено вызывается при вызове метода str()
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
class Car_5:

    def __init__(self, speed = 0, color = None):
        self.speed = speed
        self.color = color


    def increase_speed(self, delta):
        if self.speed + delta < 200:
            self.speed += delta
        else:
            self.speed = 200

    def __str__(self):
        return "<Car color: " + self.color + "; speed: " + str(self.speed) + ">"


c = Car_5(50, "red")
c.increase_speed(100)
print(c.speed, c.color)  #   150 red

d = Car_5()
d.increase_speed(100)
print(d.speed, d.color)  #   100 None

c = Car_5(50, "red")
d = Car_5(100, "blue")
print(c, d)  #   <Car color: red speed: 50> <Car color: blue speed: 100>

#Комманда __repr__ используется для некого служебного вида !!! Надо почитать!!
#Например в Питоновсой консоли:
#    a = "abc"
#    а
#        'abc' - это и есть вызов repr()
#    print(a)
#        abc - это результат работы str()

e = str(c) + str(d)
print(e)    #   <Car color: red; speed: 50><Car color: blue; speed: 100>
c.aaa ="bbb"    #Это говорит, что в питоне к конкретной машине можно приделать пятое колесо.
                #У других машин этого пятого колеса естественно не будет.
print(c)        #   <Car color: red; speed: 50>
print(c.aaa)    #   bbb

c.increase_speed(50)    #это сокращение от следующего выражения
Car_5.increase_speed(c, 50)    #Можно записывать и так
print(c)        #   <Car color: red; speed: 150>


#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
class Car_6:

    MAX_SPEED = 200

    def __init__(self, speed = 0, color = None):
        self.speed = speed
        self.color = color


    def increase_speed(self, delta):
        if self.speed + delta < self.MAX_SPEED:
            self.speed += delta
        else:
            self.speed = self.MAX_SPEED

    def __str__(self):
        return "<Car color: " + self.color + "; speed: " + str(self.speed) + ">"


c = Car_6(50, "red")
c.increase_speed(500)
print(c.speed, c.color)  #   200 red

Car_6.MAX_SPEED = 300   #Меняем константное значение класса
c.increase_speed(500)
print(c.speed, c.color)  #   300 red

d = Car_6(150, "blue")
d.increase_speed(500)
print(d)    #   <Car color: blue; speed: 300>

d = Car_6(150, "blue")
d.MAX_SPEED = 200      #Меняем значение объекта "d"
d.increase_speed(500)
print(d)    #   <Car color: blue; speed: 200>

print(c)    #   <Car color: red; speed: 300>

c.MAX_SPEED = 400   #Меняем значение объекта "d"
c.increase_speed(500)
print(c)    #   <Car color: red; speed: 400>

#У объекта могут быть свои поля и у класса есть свои поля, поля класса используются только тогда когда у объекта нет такого поля!!!
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
class Wheel:

    radius = 500

    def rotate(self):
        pass

class Car_7:

    MAX_SPEED = 200

    def __init__(self, speed = 0, color = None):
        self.speed = speed
        self.color = color
        self.wheel = [Wheel(),Wheel(),Wheel(),Wheel(),]

    def increase_speed(self, delta):
        if self.speed + delta < self.MAX_SPEED:
            self.speed += delta
        else:
            self.speed = self.MAX_SPEED

    def __str__(self):
        return "<Car color: " + self.color + "; speed: " + str(self.speed) + ">"

c = Car_7(50, "red")

print(c.wheel[0].radius)   #   500
print(c.wheel[0].rotate)   #   <bound method Wheel.rotate of <__main__.Wheel object at 0x0113EF70>>
print(c.wheel[0].rotate()) #   None
c.wheel[1].rotate()
c.wheel[2].rotate()
c.wheel[3].rotate()
def f(x):
    print(id(x))    #   17858480 Убеждаемся, что это один и тотже объект.
    x.speed = 100


f(c)
print(id(c))    #   17858480 Убеждаемся, что это один и тотже объект.
print(c)    #   <Car color: red; speed: 100>
#При передачи в функцию объекта можно менять любой аттрибут этого объекта.

#   Создаём копию объекта
print(id(c), id(d)) #   Один и тотже объект 18191600 18082608

import copy
d = copy.deepcopy(c)

print(id(c), id(d)) #   Разные объекты  18191600 18083568
print(id(c.wheel), id(d.wheel)) #   Разные масивы в объектах  18215840 17723560
print(id(c.wheel[0]), id(d.wheel[0])) #   Разные элементы в масивах в объектов  18083760 18751536
#-------------------------------------------------------------------------------

#Наследование
#-------------------------------------------------------------------------------
class PoliceCar(Car_7):
    def wawwaw(self):
        self.migalka = True

    def __str__(self):
        return "<POLICECar color: " + self.color + "; speed: " + str(self.speed) + ">"

c = PoliceCar(50, "white")  #   <POLICECar color: white; speed: 50>
d = Car_7(50, "red")
print(c)
print(c.MAX_SPEED)  #   200


#-------------------------------------------------------------------------------

class Man:
    pass
class Car_10:

    def change_driver(self, new_driver):
        self.driver = new_driver

Ivan = Man()
Petr = Man()

merz = Car_10()
merz.driver = Ivan
merz.change_driver(Petr)


def main():
    pass

if __name__ == '__main__':
    main()


#   Что такое eval (выполнение любых python скриптов)   ???