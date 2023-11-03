import vehicle
from typing import Optional


class Car(vehicle.Vehicle):
    def __init__(self, 
                 speed: float, color: str, manf: str,
                 wheels: int, engine: str, horn: Optional[str] = None):
        super().__init__(speed, color, manf, horn)
        self.wheels, self.engine = wheels, engine
    def move(self, target: str, distance: float, surface: str):
        if surface in self.surface:
            super().move(target, distance)
        else:
            print(f'{self.__class__.name__} yt vj;tn ldbufnmcz gj gjdth[yjcnb {surface}]')
another_car = Car(100, 'синий', 'Renault', 4, '*crack*')
another_car.beep()
another_car.move