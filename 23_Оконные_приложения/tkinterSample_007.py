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

v = StringVar()
ent1 = Entry (  root,
                textvariable = v,
                bg = "black",
                fg = "white"
             )

ent2 = Entry (  root,
                textvariable = v
             )

ent1.pack()
ent2.pack()

root.mainloop()
