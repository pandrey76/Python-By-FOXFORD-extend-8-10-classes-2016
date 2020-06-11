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
from random import randint

root = Tk()

field = [[None] * 4 for i in range(4)]  #странная конструкция определения
                                        #двумерного масива.
for i in range(4):
    Label(root, text = "        ", font = "Arial 48").grid(row = 4, column = i)
    Label(root, text = "", font = "Arial 48").grid(row = i, column = 4)

def add_tile(event):
    try:
        i, j = randint(0, 3), randint(0, 3)
        if not field[i][j]:
            if randint(1, 10) <= 9 :#С вероятностью 70% добавляем 2, а 30% добавляем 4.
                field[i][j] = Label( root, text = "2", font = "Arial 48", bg = "lightblue")
                field[i][j].grid(row = i, column = j)
            else:
                field[i][j] = Label( root, text = "4", font = "Arial 48", bg = "lightblue")
                field[i][j].grid(row = i, column = j)
        else:
            add_tile(event)
    except RuntimeError:
        pass

def left(event):
    for i in range(4):
        for j in range(1, 4):
            if field[i][j]:
                k = j -1
                while k >= 0 and not field[i][k]:
                    k -=1

                if k == -1:
                    field[i][j], field[i][0] = field[i][0], field[i][j]
                    field[i][0].grid( row = i, column = 0 )
                elif field[i][j]["text"] == field[i][k]["text"]:    #когда одинаковые числа
                    field[i][k]["text"] = str( int( field[i][k]["text"] ) * 2 )
                    field[i][j].destroy()
                    field[i][j] = None
                else:   #Когда разные числа
                    field[i][j], field[i][k + 1] = field[i][k + 1], field[i][j]
                    field[i][k + 1].grid( row = i, column = k + 1)

    add_tile(event)

def top(event):
    for j in range(4):
        for i in range(1, 4):
            if field[i][j]:
                k = i -1
                while k >= 0 and not field[k][j]:
                    k -=1

                if k == -1:
                    field[i][j], field[0][j] = field[0][j], field[i][j]
                    field[0][j].grid( row = 0, column = j )
                elif field[i][j]["text"] == field[k][j]["text"]:    #когда одинаковые числа
                    field[k][j]["text"] = str( int( field[k][j]["text"] ) * 2 )
                    field[i][j].destroy()
                    field[i][j] = None
                else:   #Когда разные числа
                    field[i][j], field[k + 1][j] = field[k + 1][j], field[i][j]
                    field[k + 1][j].grid( row = k + 1, column = j)

    add_tile(event)

def game_over():
    if None not in field[0] + field[1] + field[2] + field[3]:
        for i in range(3):
            for j in range(4):
                if (field[i][j]["text"] == field[i + 1][j]["text"]):
                    return
        for i in range(4):
            for j in range(3):
                if (field[i][j]["text"] == field[i][j + 1]["text"]):
                    return

        #print( "GAME OVER" )
#        for j in range(4):
#            for i in range(1, 4):
#                field[i][j].destroy()
        Label(root, text = "GAME OVER", font="Ariel 96").grid(row = 1, column = 0)

root.bind( "<Left>", left )
root.bind( "<Up>", top )

root.mainloop()
