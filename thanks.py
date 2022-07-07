import random
from turtle import Turtle

thank_you_notes =["Thanks, crossing roads is no joke!", "Thank you my friend!", "I almost got crushed!", "You save me!" ]

class Thanks(Turtle):
    def __init__(self):
        super(). __init__()
        self.thanks = ""
        self.hideturtle()
        self.penup()
        self.goto(0, 175)

    def thank_you(self):
        self.color("green")
        self.write(f"{random.choice(thank_you_notes)}", font=("Arial", 14, "normal"))
        