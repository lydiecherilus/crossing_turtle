from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super(). __init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-330, 175)
        self.write(f"Level: {self.level}", font=("Arial", 16, "normal") )

    def next_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", font=("Arial", 16, "normal") )

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write("Game Over", font=("Arial", 20, "normal"))
