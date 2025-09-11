"""
Доработайте класс `Vehicle`
"""

from abc import ABC

from homework_05 import exceptions


class Vehicle(ABC):

    def __init__(self, weight=2.5, fuel=21, fuel_consumption=10):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

        self._get_started = None  # флаг удачного/неудачного старта. используется для метода move

    def start(self, started):
        try:
            """ предполагаем, что метод принимает started=False/True при вызове.
                Этот метод можно использовать в логике метода move.
                Для этого заставим его возвращать True/False, а не только
                вызывать исключение в случае неудачи"""
            if not started:
                if self.fuel > 0:
                    started = True
                else:
                    raise exceptions.LowFuelError
            self._get_started = started

        except exceptions.LowFuelError:
            print('Cтарт не выполнен, мало топлива')
            self._get_started = False


    def move(self, distance):

        if self._get_started:
            total_fuel_consumption = self.fuel_consumption * distance / 100
            if self.fuel >= total_fuel_consumption:
                self.fuel -= total_fuel_consumption
                return self.fuel
            else:
                raise exceptions.NotEnoughFuel
        else:
            raise exceptions.DoNotStart # дополнительное исключение для невыполненного старта

v=Vehicle()
v.start(True)
""" стартуем - единственный неудачный старт: fuel=0, start=False.
    если fuel=0, start=True, то считаем, что удачный старт выполнен ранее, а на данный момент
    просто кончилось топливо.
    далее в методе move считаем дорогу
    """
try:
    print(f'К концу поездки останется {v.move(200)} топлива') # если доедем
except exceptions.NotEnoughFuel: # если не хватит до конца
    print( 'не доедем')
except exceptions.DoNotStart:
    print('даже не думай') # если даже не стартовали
