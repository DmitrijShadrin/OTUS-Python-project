from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):

    weight: None
    started: None
    fuel: None
    fuel_consumption: None

    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        super().__init__()
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel <= 0:
                raise LowFuelError
        self.started = True

    def move(self, distance):
        n = distance * self.fuel_consumption
        if n > self.fuel:
            raise NotEnoughFuel
        self.fuel -= n
