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

#
from tkinter import *
import random

#canvas - холст

colors = ["red", "green", "yellow", "blue", "black"]
def change_color(event):
    canvas.create_oval ( [50, 150],
                         [150, 50],
                         fill = random.choice(colors),
                         outline = "yellow"
                       )

root = Tk()
canvas = Canvas ( root )
canvas.create_line ( 5, 5, 50, 80 )
canvas.create_line ( 50, 80, 100, 100 )
canvas.create_line ( 100, 100, 5, 5 )
#canvas.create_oval ( [50, 150],
#                     [150, 50],
#                     fill = "red",
#                     outline = "yellow"
#                   )
canvas.pack()

but = Button ( root,
               text = "Change color",
             )
but.bind ( "<Button-1>", change_color )
but.pack()

root.mainloop()


def main():
    pass

if __name__ == '__main__':
    main()
