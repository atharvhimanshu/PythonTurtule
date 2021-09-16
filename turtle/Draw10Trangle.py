

from turtle import Turtle
r=Turtle()

lenght = 150
for x in range(3):
    lenght = lenght + 50
    r.forward(lenght)
    r.left(120)
    r.forward(lenght)
    r.left(120)
    r.forward(lenght)
    r.penup()
    r.forward(50)
    r.right(60)
    r.forward(50)
    r.right(180)
    r.pendown()



input("enter")
exit()