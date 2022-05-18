import turtle as t
import random

directions = [0, 90, 180, 270]

oz = t.Turtle()
t.colormode(255)
oz.speed(10)
oz.width(12)

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
def random_walk(movements):
    for steps in range(movements):
        oz.color(random_colour())
        oz.setheading(random.choice(directions))
        oz.forward(100)


random_walk(100)


