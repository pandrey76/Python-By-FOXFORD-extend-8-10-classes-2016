#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     13.11.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import socket
import time

sock = socket.socket()
sock.bind( ("", 12345) )
sock.listen(5)
def send_answer(conn, status = "200 OK", typ="text/plain; charset=utf-8", data = ""):
    data = data.encode("utf-8")
    conn.send(b'HTTP/1.1 ' + status.encode("utf-8") + b'\r\n')
    conn.send(b'Server: simplehttp\r\n')
    conn.send(b'Connection: close\r\n')
    conn.send(b'Content-Type: ' + typ.encode("utf-8") + b'\r\n')
    conn.send(b'Content-Lenght: ' + bytes(len(data)) + b"\r\n\r\n")
    conn.send(data)

def parse(conn, addr):
    data = b""
    while not b'\r\n\r\n' in data:
        tmp = conn.recv(1024)
        if not tmp:
            break
        else:
            data += tmp
    data = data.decode("utf-8")
    print(data)
    #data = data.split('\r\n', 1)[0]
    data = data.split('\r\n')[0]
    print(data)
    addres = data.split(' ')[1]
    print(addres)
    if addres != "/time.html":
        send_answer(conn, "404 Not Found", data = "Не найдено")
        return
    answer = """ <!DOCTYPE HTML>
    <html>
        <head>
            <title>
                Время
            </title>
        </head>
        <body>
            <h1>
            """ + time.strftime("%H:%M:%S") + """
            </h1>
        </body>
        """
    send_answer(conn, typ = "text/html; charset=utf-8", data = answer)
while 1:
    conn, addr = sock.accept()
    print("New connection " + addr[0])
    parse(conn, addr)

sock.close()

