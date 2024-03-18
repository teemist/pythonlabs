import sys


class Garage:
    def __init__(self):
        self.cars = []
        self.size = sys.getsizeof(self.cars)

    def add(self, vehicle):
        self.cars.append(vehicle)

    def remove(self, vehicle):
        self.cars.remove(vehicle)

    def show_cars(self):
        for car in self.cars:
            print(car.model)
