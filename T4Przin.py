#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 14:01:20 2020

@author: mhimanshu
"""

from turtle import Turtle
t=Turtle()

t.penup()
t.forward(300)
t.left(90)
t.forward(280)
t.left(90)
t.pendown()

oldx = t.xcor();
oldy = t.ycor();

print("coord=", oldx, ",", oldy)
t.speed(10)
for x in range(2):
    if x%2 == 1:
        t.color("red")
    else:
        t.color("green")
    
    t.forward(500)  
    t.penup()
    t.left(90)
    t.forward(20)
    t.pendown()
    t.left(90)
    t.forward(500)
    t.penup()
    t.right(90)
    t.forward(20)
    t.pendown()
    t.right(90)

t.up() 
t.setpos(oldx, oldy)
t.down() 
for x in range (7):
    t.left(90)
    t.forward(500)
    t.penup()
    if x%2 == 1:
        t.color("red")
        t.left(90)
        t.forward(20)
    else:
        t.color("green")
        t.right(90)
        t.forward(20)
        t.left(180)
    t.pendown()
    print("22")
    
    


input("enter")
exit()