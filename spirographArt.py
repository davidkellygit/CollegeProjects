## Program to create a spirograph drawing that looks like the sun.
##
## Author: David Kelly
## Date: 14 Oct 2020


import turtle
import math

d = turtle.Turtle()
d.speed(10)


# Repeat the following code to create a spirograph effect.
for i in range(300):

    # Give the drawing its yellow colour.
    d.color("yellow")

    # Move the pen a proportional distance to i.
    d.forward(i**1.25)

    # Angle it to come back around.
    d.left(175)

