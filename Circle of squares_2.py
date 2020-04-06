# CIRCULE OF SQUARES 2º método

import turtle

turtle.speed(0)

def square(l, a):
    for i in range(4):
        turtle.forward(l)
        turtle.left(a)

for i in range(36):
    square(100, 90)
    turtle.left(10)

# recomeça uma nova série
for i in range(200):
    square(100, 90)
    turtl.left(11)
