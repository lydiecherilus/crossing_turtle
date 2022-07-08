import random
from turtle import Turtle

class Cars(Turtle):
    def __init__(self, shape):
        super(). __init__()
        self.hideturtle()
        self.initial_speed = 7
        self.enemy_cars = []
        self.friendly_cars = []

    def create_enemy_cars(self):
        random_chance = random.randint(1, 12)
        if random_chance == 1 or random_chance == 7:
            enemy_car = Turtle()
            enemy_car.penup()
            enemy_car.shape("square")
            enemy_car.color(random.choice(["red", "blue", "green", "yellow", "purple", "orange"]))
            enemy_car.shapesize(stretch_wid=.75, stretch_len=2)
            enemy_car.goto(352, random.randint(-150, 150))
            enemy_car.setheading(180)
            self.enemy_cars.append(enemy_car)

    def create_friendly_cars(self):
        random_chance = random.randint(1, 30)
        if random_chance == 1:
            friend_car = Turtle()
            friend_car.penup()
            friend_car.shape("square")
            friend_car.color("black")
            friend_car.shapesize(stretch_wid=.75, stretch_len=1.75)
            friend_car.goto(352, random.randint(-150, 150))
            friend_car.setheading(180)
            self.friendly_cars.append(friend_car)
    