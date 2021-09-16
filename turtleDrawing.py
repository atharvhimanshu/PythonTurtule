#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 13:57:41 2020

@author: mhimanshu

"""


from turtle import Turtle 



A=input("enter your name here:")

b=input("enter your age")

#####################################
t2 = Turtle()
t2.speed(0)
def myup():
    t2.fd(10)

def myright():
    t2.rt(90)

def mydown():
    t2.bk(10)
    
def myleft():
    t2.left(90)
    
t2.penup()
t2.right(91)
t2.forward(100)
t2.left(91)
t2.pendown()
t2.shape('turtle')


t2.screen.onkeypress(myup, "Up")
t2.screen.onkeypress(myright, "Right") 
t2.screen.onkeypress(mydown, "Down")
t2.screen.onkeypress(myleft, "Left") 
t2.screen.listen()
################################

t = Turtle()

t.shape('turtle')
t.speed(0)
t.forward(100)

def up():
    t.fd(10)

def right():
    t.rt(90)
def down():
    t.bk(10)

def left():
    t.left(90)
t.penup()
t.right(91)
t.forward(100)
t.left(91)
t.pendown()
t.shape('turtle')


t.screen.onkeypress(up, "w")
t.screen.onkeypress(right, "d") 
t.screen.onkeypress(down, "s")
t.screen.onkeypress(left, "a") 
t.screen.listen()

t.screen.mainloop()

input("enter")
exit()