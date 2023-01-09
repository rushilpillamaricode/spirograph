import turtle
from turtle import Screen
import random 

t = turtle.Turtle()

turtle.colormode(255) 
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color
t.speed("fastest")

def spirograph(sizeofgap):
    for _ in range(int(360/sizeofgap)):
        t.circle(100)
        t.color(random_color())
        t.setheading(t.heading() + sizeofgap)
        
        
spirograph(5)        
s = Screen()
s.exitonclick()