#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     24.10.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *

root = Tk()

but = Button (  root,
                text = "Это кнопка",   #надпись на кнопке
                width = 30, height = 5, #Ширина и высота
                bg = "white", fg = "blue"   #Цвет фона и цвет надписи (текста)
             )
but.pack()

lab = Label (   root,
                text = "Это метка! \n Из двух строк.",
                font = "Ariel 18"
            )
lab.pack ( side = LEFT )

ent = Entry (   root,
                width = 20,
                bd = 30         #border - ширина оправы окна ввода
                #bd = 0          #Стандартное окно ввода текста
            )
ent.pack ( side = RIGHT )

tex = Text (    root,
                width = 40, height = 10,#Штрина-число символов в строке,Высота - число строк.
                font = "Verdana 12",
                wrap = WORD #перенос по словам
           )
tex.pack()

var = IntVar()  #Связующий объект, который связан с тремя Radiobutton в одну и
                #в другую сторону, т.е мы можем программно меняя значение IntVar
                #менять состояние отображения активной кнопки и выберая через
                #элемент управления ту или иную кнопку меняем значение переменной IntVar.

var.set(2)
rad0 = Radiobutton ( root,
                     text = "Первая",
                     variable = var,
                     value = 0
                     )
rad1 = Radiobutton ( root,
                     text = "Вторая",
                     variable = var,
                     value = 1
                     )
rad2 = Radiobutton ( root,
                     text = "Третья",
                     variable = var,
                     value = 2
                     )
rad0.pack( side = TOP )
rad1.pack( side = TOP )
rad2.pack( side = TOP )

c1 = IntVar()
c1.set(0)
c2 = IntVar()
c2.set(2)
che1 = Checkbutton ( root,
                     text = "Первый флажок",
                     variable = c1,
                     onvalue = 2,
                     offvalue = 0
                   )
che2 = Checkbutton ( root,
                     text = "Второй флажок",
                     variable = c2,
                     onvalue = 2,
                     offvalue = 0
                   )

che1.pack( side = BOTTOM )
che2.pack( side = BOTTOM )

langs = ["Linux", "Python", "Tk", "Tkinter"]
lis = Listbox ( root,
                selectmode = SINGLE,
                height = 4
              )
for lang in langs:
    lis.insert( END, lang )

lis.pack ( side = TOP )
root.mainloop()

