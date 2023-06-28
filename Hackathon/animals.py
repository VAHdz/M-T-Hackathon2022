"""
Animals teehee
"""

from turtle import *

# panda


def ring(col, rad):
    # Set the fill
    fillcolor(col)
    # Start filling the color
    begin_fill()
    # Draw a circle
    circle(rad)

    # Ending the filling of the color
    end_fill()


def panda(x, y):
    hideturtle()
    speed(0)
    up()
    setpos(x, y)
    forward(300)
    left(90)
    forward(80)
    right(90)
    forward(40)
    down()
    ring('black', 15)
    up()
    back(80)
    down()
    ring('black', 15)
    up()
    setpos(x, y)
    forward(300)
    down()
    ring('white', 55)
    up()
    left(90)
    forward(50)
    right(90)
    forward(20)
    down()
    ring('black', 8)
    ring('white', 4)
    up()
    back(40)
    ring('black', 8)
    ring('white', 4)
    up()
    setpos(x, y)
    forward(300)
    left(90)
    forward(40)
    right(90)
    down()
    ring('black', 5)
    right(90)
    circle(5, 180)
    up()
    setpos(x, y)
    right(90)
    forward(300)
    left(90)
    forward(40)
    down()
    left(360)
    circle(5, -180)
    up()
    setpos(x, y)


# India Flag


def india(x, y):
    speed(0)
    # hideturtle()
    up()
    setpos(x, y)
    down()
    left(90)
    pencolor("green")
    fillcolor("green")
    begin_fill()
    for i in range(2):
        forward(40)
        right(90)
        forward(200)
        right(90)
    end_fill()
    up()
    forward(80)
    fillcolor("orange")
    begin_fill()
    for i in range(2):
        forward(40)
        right(90)
        forward(200)
        right(90)
    end_fill()
    up()
    back(40)
    right(90)
    forward(100)
    color("blue")
    begin_fill()
    circle(20)
    end_fill()
    left(90)
    forward(4)
    right(90)
    color("white")
    begin_fill()
    circle(16)
    end_fill()
    left(90)
    forward(16)
    right(90)
    color("blue")
    begin_fill()
    down()
    for j in range(24):
        forward(15)
        backward(15)
        left(15)
    end_fill()
    up()
    setpos(x, y)
    pencolor("black")


# Mexico: Sun and Pyramid


def triangle(size):
    forward(size)
    left(105)
    forward(size*2)
    left(150)
    forward(size*2)
    right(75)


def triangle2(size):
    triangle(size)
    left(10.28)
    forward(size)
    right(180)


def pyramid():
    for i in range(5):
        left(90)
        forward(20)
        left(90)
        forward(20)
        right(180)
    left(180)
    for i in range(5):
        left(90)
        forward(20)
        right(90)
        forward(20)


def pyramid2():
    for i in range(5):
        left(90)
        forward(20)
        right(90)
        forward(20)
        # left(180)


def mexico(x, y):
    hideturtle()
    up()
    setpos(x, y)
    left(90)
    forward(140)
    right(90)
    forward(100)
    down()
    color("yellow")
    speed(0)
    begin_fill()
    for i in range(25):
        triangle(7.2)
        left(14.4)
        forward(7.2)
        right(180)
    end_fill()
    up()
    setpos(x, y)
    forward(20)
    down()
    color("orange")
    begin_fill()
    forward(180)
    pyramid()
    end_fill()
    pencolor("white")
    back(20)
    up()
    pencolor("black")
    setpos(x, y)
