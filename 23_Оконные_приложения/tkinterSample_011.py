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

#Geometry Manager Greed определяет длину столбца и высоту строки по самому большому элементу.
from tkinter import *

root = Tk()

but = Button (  root,
                text = "Это кнопка",   #надпись на кнопке
                width = 30, height = 5, #Ширина и высота
                bg = "white", fg = "blue"   #Цвет фона и цвет надписи (текста)
             )
but.grid ( row = 1, column = 1 )

lab = Label (   root,
                text = "Это метка! \n Из двух строк.",
                font = "Ariel 18"
            )
lab.grid ( row = 2, column = 1 )

ent = Entry (   root,
                width = 20,
                bd = 30         #border - ширина оправы окна ввода
                #bd = 0          #Стандартное окно ввода текста
            )
ent.grid ( row = 3, column = 1 )

tex = Text (    root,
                width = 40, height = 10,#Штрина-число символов в строке,Высота - число строк.
                font = "Verdana 12",
                wrap = WORD #перенос по словам
           )

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
rad0.grid ( row = 4, column = 1 )
rad1.grid ( row = 4, column = 2 )
rad2.grid ( row = 4, column = 3 )

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

che1.grid ( row = 2, column = 2 )
che2.grid ( row = 2, column = 3 )

langs = ["Linux", "Python", "Tk", "Tkinter"]
lis = Listbox ( root,
                selectmode = SINGLE,
                height = 4
              )
for lang in langs:
    lis.insert( END, lang )

lis.grid ( row = 2, column = 4 )
root.mainloop()

