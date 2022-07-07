import time
from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import Scoreboard
from thanks import Thanks

# setup screen
screen = Screen()
screen.bgcolor("white")
screen.setup(width=700, height=400)
screen.title("Turtle Crossing")

# create player
turtle_body = Player("turtle")

# create enemy cars (all colors) and friendly cars (black)
cars = Cars()

# create scoreboard to show player's score
scoreboard = Scoreboard()

# create thank you note
thanks = Thanks()


screen.exitonclick()
