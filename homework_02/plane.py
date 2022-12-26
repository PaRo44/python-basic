from homework_02.base import Vehicle
from homework_02 import exceptions


class Plane(Vehicle):
    cargo: 0
    max_cargo: 0

    def __init__(self, max_cargo, weight, fuel, fuel_consumption):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, num):
        if (num + self.cargo) <= self.max_cargo:
            self.cargo += num
        else:
            raise exceptions.CargoOverload

    def remove_all_cargo(self):
        cargo = self.cargo
        self.cargo = 0
        return cargo
