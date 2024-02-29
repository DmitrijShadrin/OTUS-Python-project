"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload

class Plane(Vehicle):
    cargo: None
    max_cargo: None

    def __init__(self, weight: int, fuel: int, fuel_consumption: int, max_cargo: int):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, value: int):
        n = self.cargo + value
        if n > self.max_cargo:
            raise CargoOverload
        self.cargo += value

    def remove_all_cargo(self):
        n = self.cargo
        self.cargo = 0
        return n
