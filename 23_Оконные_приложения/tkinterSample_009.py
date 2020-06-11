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

def new_win():
    Toplevel(root)

def close_win():
    root.destroy()

def about():
    win = Toplevel(root)
    lab = Label ( win,
                  text = "Это просто программа-тест \n меню в Tkinter"
                )
    lab.pack()
root = Tk()

m = Menu(root)  #создаётся объект меню на главном окне

root.config ( menu = m )    #окно конфигурируется с указанием меню для него

fm = Menu(m)    #Создаётся пункт меню с размещением на основном меню (m)
m.add_cascade(label = "File", menu = fm)    #пункт располагается на основном меню (m)
fm.add_command ( label="New", command = new_win)   #Формируется список команд пункта меню
fm.add_command ( label="Open...")
fm.add_command ( label="Save...")
fm.add_command ( label="Exit", command = close_win )

hm = Menu(m)    #Второй пункт меню
m.add_cascade ( label="Help", menu = hm )
hm.add_command ( label="Help" )
hm.add_command ( label="About", command = about )

root.mainloop() #Цикл обработки сообщений не создаётся для отдельного окна
                #(например:TopLevel окна), а создаётся для всей программы в
                #целом и в нем мы будем отлавливать сообщения в том числе из дочерних окон