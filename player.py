from turtle import Turtle

class Player(Turtle):
    def __init__(self, shape):
        super(). __init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -180)
        self.right(270)
