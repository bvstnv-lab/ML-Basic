"""
Создайте класс `Plane`, наследник `Vehicle`
"""
from homework_05 import base
from homework_05 import exceptions

class Plane(base.Vehicle):
    def __init__(self, weight, fuel, fuel_consumption):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo=10
        self.max_cargo=15

    def load_cargo (self, load):
        current_load=self.cargo+load
        if self.max_cargo>current_load:
            self.cargo=current_load
        else:
            raise exceptions.CargoOverload

    def remove_all_cargo(self):
        removed_cargo=self.cargo
        self.cargo=0
        return removed_cargo