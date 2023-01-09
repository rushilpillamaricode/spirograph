import turtle
import random 

t = turtle.Turtle()
turtle.colormode(255) 
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color

directions = [0,90,180,270]
t.pensize(5)
t.speed("fastest")
for i in range(500):
    t.color(random_color()) 
    t.forward(20)
    t.setheading(random.choice(directions))