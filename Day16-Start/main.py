from turtle import Turtle, Screen
import Anothermodule

timmy = Turtle()

timmy.shape("turtle")
my_screen = Screen()
timmy.color("DarkSlateGray1")
timmy.forward(100)
print(my_screen.canvheight)
my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)