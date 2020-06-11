#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     27.10.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *

root = Tk()

m = Menu(root)  #создаётся объект меню на главном окне

root.config ( menu = m )    #окно конфигурируется с указанием меню для него

fm = Menu(m)    #Создаётся пункт меню с размещением на основном меню (m)
m.add_cascade(label = "File", menu = fm)    #пункт располагается на основном меню (m)
fm.add_command ( label="New")   #Формируется список команд пункта меню
fm.add_command ( label="Open...")
fm.add_command ( label="Save...")
fm.add_command ( label="Exit")

hm = Menu(m)    #Второй пункт меню
m.add_cascade ( label="Help", menu = hm )
hm.add_command ( label="Help" )
hm.add_command ( label="About" )

root.mainloop()