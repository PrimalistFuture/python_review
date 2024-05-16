from prettytable import PrettyTable  # package installed
from turtle import Turtle, Screen  # came pre-installed with Python

# OOP
# object  class
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# timmy.left(90)


# my_screen = Screen()
# my_screen.exitonclick()


# Package
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)
