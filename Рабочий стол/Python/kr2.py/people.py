from typing import Optional
from abc import ABC, abstractmethod

from car import Car
from utils import Position, InsufficientFunds, CarAbscentError

class Person(ABC):
    @abstractclassmethod
    def __init__(self, name: str, position: Optional[Position] = None) -> None:
        self.__user_score = []
        self.__position = position if position else Position()
        self.name = name
    
    @property
    def position(self) -> Position:
        return self.__position
    
    @position.setter
    def position(self, new_position: Position) -> None:
        if not isinstance(new_position, Position):
            raise TypeError(f'Position should be Position instance, not {type(new_position).__name__}')
        self.__position = new_position
    
    @property
    def rating(self) -> float:
        last_rids = self.__user_score[-40:]
        return round(sum(last_rids) / len(last_rids), 2) if self.__user_score else 5.
    
    def __str__(self) -> str:
        return f'{self.__class__.__name__} {self.name}, rating: {self.rating}'
    class Client(Person):
    def __init__(self, name: str, balance: float, position: Optional[Position] = None) -> None:
        super().__init__(name, position)
        self.balance = balance
        
    @property
    def balance(self) -> float:
        return self.__balance
    
    @balance.setter
    def balance(self, new_balance: float) -> None:
        if not isinstance(new_balance, float):
            raise TypeError(f'new balance value should be float, not {type(new_balance).__name__}')
        if new_balance < 0:
            raise ValueError(f'cannot set negative value as balance')
        self.__balance = new_balance

    def pay(self, amount: float) -> None:
        if self.balance < amount:
            raise InsufficientFounds(amount, self)
        self.balance -= amount
    
