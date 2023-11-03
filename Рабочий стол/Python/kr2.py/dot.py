#точка на декартовой плоскости
from typing import Self
from random import randint
import math
class Dot:
    __counter = 0
    def __init__(self, x: int=0, y: int = 0)->None:
        self.x, self.y = x,y
        self.__class__.__counter +=1
    def __str__(self):
        return f'Dot with x={self.x}, y={self.y}'
    def __gt__(self, other: Self)-> bool:
        return self.x >other.x and self.y > other.y
    def __lt__(self, other: Self)->bool:
        return self.x < other.x and self.y < other.y
    def __eq__(self, other:Self)->bool:
        return self.x==other.x and self.y == other.y
    def __ne__(self, other: Self)->bool:
        return not self.__eq__(other)
    def __add__(self, other:Self)->Self:
        return Dot(self.x + other.x, self.y + other.y)
    def __sub__(self, other:Self)->Self:
        return Dot(self.x - other.x, self.y - other.y)
    @classmethod
    def get_counter(cls):
        return cls.__counter
    def __del__(self):
        self.__class__.__counter -=1
        del self
dots= [Dot(randint(0,3), randint(0,3)) for _ in range(4)]
    
print(Dot(3,3)>Dot(1,1))
print(Dot(1,1)+ Dot(3,3))
   



# sin_dots = [Dot(x, round(math.sin(x))) for x in range(10)]
# print([str(dot) for dot in sin_dots])
