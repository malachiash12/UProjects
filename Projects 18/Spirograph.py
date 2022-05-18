import turtle as t
import random

directions = [0, 90, 180, 270]

#Creates a turtle object named 'oz' with the following attributes. 'colormode' allows rgb color values:
# setting max values in the rgb tuple to 255
spiro = t.Turtle()
t.colormode(255)
spiro.speed("fastest")
spiro.width(7)

#Creates a random rgb colour value
def random_colour():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_spirograph(size_of_gap):
    for steps in range(int(360/size_of_gap)): #Ensures the correct amount of circles are drawn depending on the gap angle
        spiro.color(random_colour())
        spiro.circle(100) # draws a circle of radius 100
        spiro.setheading(spiro.heading()+size_of_gap) # changes the tilt of the circle drawn by the 'size of gap' angle


draw_spirograph(5)

#Allows the screen generated to exit on click
screen = t.Screen()
screen.exitonclick()
