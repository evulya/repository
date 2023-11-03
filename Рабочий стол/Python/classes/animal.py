from typing import Optional
class Animal:
    sound: str
    def __init__(self, age: int, name: Optional[str]=None):
        self.age, self.name =age, name
    def voice(self)-> None:
        print(self.sound)
    def get_sleeping(self)->None:
        print(f'{self.__class__.__name__} {self.name} is {"" if self.sleeping else "not"} sleeping')

class Cat(Animal):
    sound: str = 'meow (hiss)'
    def do_not_sleep(self):
        self.sleeping =True
    def sleep(self):
        self.sleeping =False
class Dog(Animal):
    sound: str ='bark (woof)'
my_cat = Cat(1, 'Вездескок')
my_cat.sleep()
my_cat.get_sleeping()