#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 12:44:30 2020

@author: mhimanshu
"""

from turtle import Turtle
t=Turtle()

for x in range(50):
    t.forward(100)
    t.penup()
    t.right(90)
    t.forward(100)
    t.pendown()
    t.right(90)
    t.forward(100)
    t.right(10)
    t.forward(100)
    t.penup()
    t.right(90)
    t.forward(100)
    t.pendown()
    t.right(90)
    t.forward(100)

input("entar")
exit()