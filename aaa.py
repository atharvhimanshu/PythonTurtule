#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 11:19:28 2020

@author: mhimanshu
"""

from turtle import Turtle 

t =Turtle()
t.speed(0)

t2 = Turtle()
t2.setpos(100,100)
t2.color("red")
t2.speed(10)

for x in range(10,50):
    t.forward(x*2)
    t.left(91)
    
    t2.forward(x*2)
    t2.left(91)    
    
input("enter")
exit()