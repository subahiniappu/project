import turtle
import time

screen = turtle.getscreen()

screen.bgcolor("#b3daff")

screen.title("Indian Flag - https://www.pythoncircle.com")

oogway = turtle.Turtle()

oogway.speed(50)
oogway.penup()

oogway.shape("turtle")

flag_height = 300
flag_width = 450

start_x = -225
start_y = 150

stripe_height = flag_height/3
stripe_width = flag_width

chakra_radius = stripe_height / 2

def draw_fill_rectangle(x, y, height, width, color):
    oogway.goto(x,y)
    oogway.pendown()
    oogway.color(color)
    oogway.begin_fill()
    oogway.forward(width)
    oogway.right(90)
    oogway.forward(height)
    oogway.right(90)
    oogway.forward(width)
    oogway.right(90)
    oogway.forward(height)
    oogway.right(90)
    oogway.end_fill()
    oogway.penup()


def draw_stripes():
    x = start_x
    y = start_y
   
    draw_fill_rectangle(x, y, stripe_height, stripe_width, "#FF9933")
   
    y = y - stripe_height   
   
    draw_fill_rectangle(x, y, stripe_height, stripe_width, "white")
    y = y - stripe_height               

    
    draw_fill_rectangle(x, y, stripe_height, stripe_width, '#138808')
    y = y - stripe_height


def draw_chakra():
    oogway.speed(1)
    oogway.goto(0,0)
    color = "#000080" # navy blue
    oogway.penup()
    oogway.color(color)
    oogway.fillcolor(color)
    oogway.goto(0, 0 - chakra_radius)
    oogway.pendown()
    oogway.circle(chakra_radius)
    # draw 24 spikes in chakra
    for _ in range(24):
        oogway.penup()
        oogway.goto(0,0)
        oogway.left(15)
        oogway.pendown()
        oogway.forward(chakra_radius)
  
    
time.sleep(0)

draw_stripes()

draw_chakra()

oogway.hideturtle()

screen.mainloop()

