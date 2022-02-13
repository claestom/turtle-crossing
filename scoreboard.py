from turtle import Turtle

FONT = ("Courier", 24, "normal")
SPEED_INCREASE_FACTOR = 0.9


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level_score = 0
        self.set_score()
        self.speed = 0.1

    def set_score(self):
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-280, 270)
        self.write(f"Level: {self.level_score}", move=False, align="left", font=FONT)

    def increase_score(self):
        self.clear()
        self.level_score += 1
        self.set_score()
        self.speed *= SPEED_INCREASE_FACTOR

    def game_over(self):
        self.clear()
        self.write(f"GAME OVER! You've reached level:{self.level_score}", move=False, align="left", font=FONT)
