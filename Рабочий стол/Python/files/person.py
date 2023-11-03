class Passport:
    def __init__(self, series: str, number: str)->None:
        self.series, self.number = series, number
    def check(self, value:str, length: int)->None:
        if not isinstance(value, str) or len(value != length or not value.isdigit()):
            raise ValueError(f'{type(value).__name__}{value} is not')
    @property
    def series(self)->str:
        return self.__series
    @series.setter
    def series(self, new_series: str)->None:
        self.check(new_series, 4)
        self.__series = new_series
class Person:
    def __init__(self, name: str, age: int, passport: str) ->None:
        self.name = name #public attribute
        self._age = age #private attribute
        self.__passport = passport #hidden attribute
    def get_age(self) ->int:
        return self._age
    def set_age(self, new_age: int)-> None:
        if not isinstance(new_age, int):
            raise TypeError(f'{type(new_age).__name__} is not int')
        if new_age<0:
            raise ValueError(f'Age {new_age} is less than zero')
        self._age = new_age
    age= property(get_age, set_age)
    @property
    def passport(self)-> Passport:
        return self.__passport
    @passport.setter
    def passport(self, new_passport) -> None:
        if not isinstance(new_passport, Passport):
            raise TypeError(f'{type(new_passport).__name__} is not a passport')
        self.__passport = new_passport

ivanov = Person('Ilya', 17, '1234 567890')
print(ivanov.age)
