#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль2
# Purpose:
#
# Author:      Prapor
#
# Created:     23.10.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *

root = Tk()
#root.geometry("200x200")    #Определяем размер окна
################################################################################
#1. Создаём объект кнопка
but = Button (  root,
                text = "Печатать",
                width = "40"
             )  #Хороший стиль написания метода с большим количеством параметров
but2 = Button(root)
but3 = Button(root)

#2. Устанавливаем её свойства
but["width"] = 20

#3. Вешаем на левый клик по кнопке функцию print_hello
def print_hello(event):
    print("Как всегда очередной 'Hello World!'")
    but["text"] += "."
    but["fg"], but["bg"] = but["bg"], but["fg"]
    #   background  foreground

    print(event)    #   <tkinter.Event object at 0x01238C50>


        #event          listener
but.bind("<Button-1>", print_hello) #Клик по левой кнопки мыши


root.bind("<Left>", print_hello)    #Нажатие на левую стрелку

#4. Размещаем кнопку на форме
#   window manager
but.pack()
but2.pack()
but3.pack()
################################################################################
root.mainloop()
