from typing import Optional
class Vehicle:
    def __init__(self, speed: float, color: str, manf: str, horn: Optional[str] = None):
        if speed <0:
            raise ValueError( '')
        self.speed = speed
        self.color = color
        self.manf = manf
        self.horn = horn
    def move(self, target: str, distance: float):
        if self.speed>0:
            hours = distance / self.speed
            day_hours = 24
            time =f'{hours} часов' if hours < day_hours else '{0:.1f} суток'.format(hours / day_hours)
            print(f'Вы прибыли в {target} за {distance / self.speed} времени')
        else:
            print(f'На этом транспорте в {target} не добраться ')
    def beep(self):
        print(self.horn if self.horn else '*silence*')
    def info(self):
        print(f'this is a {self.color}{self.__class__.__name__}{self.manf}')
gift_car = Vehicle(40, 'red', 'Flintstone', 'beep-beep')
print(gift_car.info())
gift_car.move('Магадан', 5000)
gift_car.beep()
print(type(Vehicle))