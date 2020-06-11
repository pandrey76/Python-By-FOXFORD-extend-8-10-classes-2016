#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Prapor
#
# Created:     09.11.2017
# Copyright:   (c) Prapor 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import socket

#Создаём клиентский сокет
conn = socket.socket()
conn.connect( ("127.0.0.1", 12345) )

#Пытаемся передать информацию 
conn.send(b"Hello")     #b'Hello'

conn.send(" Вася".encode("utf-8"))  # b' \xd0\x92\xd0\xb0\xd1\x81\xd1\x8f'
#При этом как работает send она сваливает данные в некоторую как бы трубу между 
#сервером и клиентом. А когда сервер хочет что то прочитать из этой трубы он 
#берёт все даные, которые пришли к этому моменту, но не больше околичества 
#ограниченного параметром метода recv.
#Достаточно приметивный протокол, один вызов клиентом метода send, на стороне 
#сервера отрабатывается одним вызовом метода recv. 
    
data = conn.recv(100)  #
print(data)             #b'Buy 2'