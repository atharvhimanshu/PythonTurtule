
from turtle import Turtle 

t =Turtle()
t.screen.bgcolor("red")
t.speed(0)

t2 = Turtle()
t2.setpos(200,200)
t2.color("red")
t2.speed(0)

for x in range(10,50):
    t.circle(x)
    t.left(91)
    
    t2.circle(x)
    t2.left(91)    
    
input("enter")
exit()