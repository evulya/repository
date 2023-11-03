#напишем игру race
#гонка при инизиализации принимает машины list(Car)
#машина Car имеет свойства: model: str, speed: float
#Гонка:
#на каждом втором круге выбывает случайная машина (случается авария)
import random 
class Car:
    def __init__(self, model: str, speed: float):
        self.model = model
        self.speed = speed
    @property
    def speed(self)-> float|int:
        return self._speed 
    @speed.setter
    def speed(self, new_speed)->None:
        if not isinstance(new_speed, (int, float)):
            raise TypeError(f'Speed {type(new_speed).__name__} of {self.model}cis not int|float')
        if new_speed <0:
            raise ValueError(f'Speed of {self.model}{new_speed}<0')
        self._speed = new_speed
class Race:
    def __init__(self, cars: list[Car], laps: int=5, crash_prob: int = 45):
        self.cars = cars
        self.laps = laps
        self.crash_prob = crash_prob
        def probability_proc(self)-> bool:
            return random.randint(0, 90)< self.crash_prob
        @property
        def cars(self)-> list[Car]:
             return self._cars
        @cars.setter
        def cars(self, new_cars: list[Car])->None:
             for car in new_cars:
                 if not isinstance(car, Car):
                     raise TypeError(f'{type(car)._name__}is not a Car instance')
            self._cars = new_cars
        def start(self):
            self.cars.sort(key=lambda car: car.speed, reverse=True)
            while self.cars and self.__counter
            while self.cars and self.__counter.value < self.laps:
models = ['Toyota Supra', 'Nissan Skyline']
cars = [Car(model, random.randint(1, 50)) for model in models]
