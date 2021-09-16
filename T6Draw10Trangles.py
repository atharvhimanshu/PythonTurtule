#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 13:14:00 2020

@author: mhimanshu
"""

from turtle import Turtle
r=Turtle()

lenght = 10
dx = 5
for x in range(40):
    lenght = lenght + dx*3
    r.forward(lenght)
    r.left(120)
    r.forward(lenght)
    r.left(120)
    r.forward(lenght)
    r.penup()
    r.forward(dx)
    r.right(60)
    r.forward(dx)
    r.right(180)
    r.pendown()
    

input("enter")
exit()