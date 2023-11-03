from typing import Any, Self, Optional
from datetime import date, timedelta
from calendar import leapdays
import json

class InvalidBirthDate(Exception):
    def __init__(self, birthdate:str):
        super().__init__(f'Given birthdate appears to be invalid: {birthdate}')

class Person:
    def __init__(self, name : str, age : int)->None:
        self.name, self.age = name, age
    @staticmethod
    def is_person_static(value:Any)->bool:
        return isinstance(value, Person)
    @classmethod
    def is_person(cls, value: any)->bool:
        return isinstance(value, cls)
    def __str__(self)->str:
        return f'{self.__class__.__name__}{self.name}{self.age}y.o'
    @classmethod
    def from_birthdate(cls, name:str, birthdate:str):
        try:
            bday = date.fromisoformat(birthdate)
        except ValueError:
            raise InvalidBirthDate(birthdate)
        today = date.today()
        age = today.year - bday.year
        if today.month < bday.month or (today.month == bday.month and today.day < bday.day):
            age -=1
    def to_dict(self)->dict:
        return{'name': self.name, 'age':self.age}
    def write_to_json(self, filename, Optional[str]=None)->None:
#list[Self] -  список объектов класса Person

































        
ivanov = Person('Ivanov', 17)
print(date.fromisoformat('1986-01-12'))
birthdate = timedelta(days=1)
print(birthdate)
ivanov = Person.from_birthdate('agent-ilusha', '1974-01-12')
ivanov= Person.from_birthdate('agent-ilusha', '1986-10-25')
print(ivanov)
# print(Person.is_person(ivanov))
# ivanov.is_person(ivanov)

