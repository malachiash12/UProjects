import turtle as t

import random

tim = t.Turtle()

colours = ["Blue", "Red", "Green", "Yellow", "Purple", "Pink", "Cyan", "Orange", "Violet", "Silver", "Brown"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for no_shape_sides in range(3,11):
    tim.color(random.choice(colours))
    draw_shape(no_shape_sides)

