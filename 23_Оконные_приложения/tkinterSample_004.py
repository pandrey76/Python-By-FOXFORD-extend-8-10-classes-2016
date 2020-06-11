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
root.mainloop()