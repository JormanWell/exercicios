# CIRCULE OF SQUARES

import turtle

turtle.speed(0)

def square():
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    
square()
turtle.left(100)

for i in range(35):
        square()
        turtle.left(100)



