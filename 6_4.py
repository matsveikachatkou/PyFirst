from random import random


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f"Speed is {self.speed}")

    def go(self):
        print("Car goes down the road")

    def stop(self):
        print("Car stopped")

    def turn(self):
        if random() < 0.5:
            print("Car turned left")
        else:
            print("Car turned right")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed < 60:
            print(f"Speed is {self.speed}")
        else:
            print("Speed limit!")


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed < 40:
            print(f"Speed is {self.speed}")
        else:
            print("Speed limit!")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


example = TownCar(45, "red", "Ford", False)
example.show_speed()
example.turn()
