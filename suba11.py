from turtle import *

from random import randint

speed(0)

bgcolor('white')

x=1

while x < 400:
    r=randint(0,255)
    g=randint(0,255)
    y=randint(0,255)

    colormode(255)

    pencolor(r,g,y)

    fd(50 + x)
    rt(90.911)

    x=x+1

exitonclick()
