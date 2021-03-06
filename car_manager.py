from turtle import Turtle
import random as r

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_chance = r.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(2, 1)
            new_car.color(r.choice(COLORS))
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.goto(260, r.randint(-260, 260))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)