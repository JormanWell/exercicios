# trinagulos

import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)

def triangle(l, a):
    for i in range(3):
        my_turtle.forward(l)
        my_turtle.right(a)

for i in range(100):
    triangle(200, 120)
    my_turtle.right(125)
    
