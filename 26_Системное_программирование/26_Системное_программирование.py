﻿#!/usr/bin/env python
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

#-------------------------------------------------------------------------------
#   Протокол
#   Стек протоколов OSI
#7. Приложения      (протокол: http)
#6. Представления данных.   (протокол: SSL )
#5. Сессия - soc
#4. Транспорт - правила по которым будут распространятся данные по сети. (протокол: TCP или UDP)
#Протокол UDP - комьпьютерные игры, потоковое видео, не вся информация сущемственна,
#но существенна скорость передачи этой информации
#3. Сеть - связанные друг  с другом клиенты.    (протокол: IP)
#2. Передача данных - структурированные данные.
#1. Физический уровень - физическая среда распростронения.

#На каждом уровни должны быть договорённости, чтобы на обоих концах было
#одинаковое оборудование и одинаковый софт.
#Протокол https - стек протоколов http и SSL.

#   Технологии обмена в Web

#   1. AJAX      -  в фоновом режиме страницы вы посылаете запрос на сервер и
#                   получаете ответ от этого сервера.

#   2. Long poll -   Long polling requests. Мы посылаем сообщение серверу с
#                    вопросом, а нет ли каких нибудь новых сообщений, например
#                    в чате. Сервер не сразу отвесает на это сообщение,
#                    а отвечает на него только в тот момент, когда действительно
#                    в чате появляется новое сообщение. Т.е. вы посылаете запрос
#                    и он висит на стороне сервера и сервер не присылает ответ
#                    и как только новое сообщение появилось он присылает ответ
#                    и вы тут же посылаете следующий запрос и этот запрос также
#                    будет висеть до следующего сообщения в чате без ответа на
#                    стороне сервера.
#   3. Web Sockets - В этой технологии мы уже устанавливаем некий канал
#                   (соединение) между моим компьютером и сервером, как мы можем
#                    передавать информацию в этот какнал, так и сервер может
#                    посылать информацию в этот канал. Самый распростроненный
#                    способ устанавливать соединение для общения, для создания
#                    компьютерных игр и т.д.
#   4. Web RTC -    технология, используемвя для доставки вам аудео/видео контента.
#                   Например мы смотрим видео нам это видео как то будет
#                   досылаться и досылаться. Технология работает как "peer to
#                   peer", т.е. она может работать без сервера, как сделано в
#                   Scype, никакого Scype сервера нет мы можем подключаться,
#                   используя какие то другие компьютеры без соединения с
#                   сервером, когда вы запускаете Scype клиент, то знайте что
#                   много совершенно незнакомых вам людей могут общаться через
#                   ваш компьютер, если у вас есть IP адрес, а у них нет, то им
#                   понадобится некий сервер для общения и ваш компьютер в фоне
#                   может стать сервером и качать довольно много информации.

#   5. Server sent events - здесь клиенты не могут просто так общаться с
#                   сервером, только сервер может посылать им информацию.
#-------------------------------------------------------------------------------

#   Уровни 7 и 6 модели OSI можно реализовать используя сокеты, т.е. мы
#   устанавливаем соединение, а дальше по нему мы можем отправлять http
#   запросы и посылать ответы на них.

