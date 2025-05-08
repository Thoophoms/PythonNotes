import tkinter
from turtle import Turtle, Screen

#
#
# my_screen = Screen()
# # print(my_screen.canvheight)
# # my_screen.bgcolor("white")
# my_screen.bgcolor("lightblue")
#
#
# soba = Turtle()
# print(soba)
# soba.shape("turtle")
# soba.color("coral")
#
# soba.forward(100)
#
#
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()
table.add_column(fieldname="Pokemon Name", column=["Pikachu", "Squirtle", "Charmander"], align="l")
table.add_column(fieldname="Type", column=["Electric", "water", "Fire"], align="l")

print(table.align)

print(table)