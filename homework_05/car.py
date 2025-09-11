"""
Создайте класс `Car`, наследник `Vehicle`
"""
from homework_05 import base
from homework_05 import engine

class Car(base.Vehicle):
    def __init__(self, weight, fuel, fuel_consumption):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine=None

    def set_engine(self,volume, pistons):
        self.engine=engine.Engine(volume, pistons)

