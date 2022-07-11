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
screen.tracer(0)

# create player
turtle_body = Player()

# create enemy cars (all colors) and friendly cars (black)
cars = Cars()

# create scoreboard to show player's score
scoreboard = Scoreboard()

# create thank you note
thanks = Thanks()

# create event listeners to move player forward and backward
screen.listen()
screen.onkey(turtle_body.move_forward, "Up")
screen.onkey(turtle_body.move_backward, "Down")


# start game
isgame_on = True
while isgame_on:
    time.sleep(0.1)
    screen.update()

    cars.create_enemy_cars()
    cars.move_enemy_cars()

    cars.create_friendly_cars()
    cars.move_friendy_cars()

    # detect collision with enemy cars
    # if player collides with enemy cars, the game is over
    for car in cars.enemy_cars:
        if car.distance(turtle_body) < 20:
            isgame_on = False
            scoreboard.game_over()
            
    # detect collision with friendy cars
    # if player collides with friendly cars (black cars), player says thanks and the game continues
    for car in cars.friendly_cars:
        if car.distance(turtle_body) < 10:
            thanks.thank_you()
           
        elif car.distance(turtle_body) > 20:
            thanks.clear()
            
    # detect successful crossing
    # if player crosses the road without getting hit, the game levels up and the speed increases 
    if turtle_body.ycor() > 180:
        turtle_body.goto(0, -180)
        cars.level_up()
        scoreboard.next_level()


screen.exitonclick()
