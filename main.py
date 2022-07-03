from turtle import Screen
from player import Player
from cars import Cars
from friends import Friends
from scoreboard import Scoreboard

# setup screen
screen = Screen()
screen.bgcolor("white")
screen.setup(width=700, height=400)
screen.title("Turtle Crossing")

# create turtle
player = Player("turtle")

# create enemy cars
cars = Cars()

# create friendly Cars
friends = Friends()

# create scoreboard
scoreboard = Scoreboard()


screen.exitonclick()
