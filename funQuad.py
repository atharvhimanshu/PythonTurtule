# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
from turtle import Turtle
import turtle

def movePenToStartPos():
    t.penup()
    t.forward(dx)
    t.left(90)  
    t.forward(dx)
    t.right(180)
    t.pendown()
    
def drawSquare(l):
    t.forward(l)
    t.right(90)
    t.forward(l)
    t.right(90)
    t.forward(l)
    t.right(90)
    t.forward(l)
    
def drawQuad(l, w):
    t.forward(l)
    t.right(90)
    t.forward(w)
    t.right(90)
    t.forward(l)
    t.right(90)
    t.forward(w)    
        
    
    
t=Turtle()
t.clear()
t.speed()

# draw boundary
t.penup()
t.backward(200)
t.left(90)
t.forward(200)
t.right(90)
t.pendown() 

drawQuad(500, 500)

#take pen to center
t.penup()
t.backward(200)
t.right(90)
t.forward(200)
t.pendown()

# end draw boundary


lenght = 120
width = 100
dx = 10

#first squar
drawQuad(lenght,width)

number = [1,2,3,4,5,6,7,8,9]
for x in number:

#a new square
movePenToStartPos()
lenght = lenght + (2*dx)
width = width+ (2*dx)
drawQuad(lenght,width)

#a new square
movePenToStartPos()
lenght = lenght + (2*dx)
width = width+ (2*dx)
drawQuad(lenght,width)

#a new square
movePenToStartPos()
lenght = lenght + (2*dx)
width = width+ (2*dx)
drawQuad(lenght,width)

#a new square
movePenToStartPos()
lenght = lenght + (2*dx)
width = width+ (2*dx)
drawQuad(lenght,width)

#a new square
movePenToStartPos()
lenght = lenght + (2*dx)
width = width+ (2*dx)
drawQuad(lenght,width)



#a new square
t.penup()
t.forward(110)
t.left(90)
t.forward(110)
t.right(90)
t.forward(40)
t.left(90)
t.forward(40)
t.pendown()

drawSquare(40)
t.left(90)
t.penup()
t.forward(540)
t.left(90)
t.forward(20)
t.pendown()
drawSquare(40)
input("enter")
exit()
