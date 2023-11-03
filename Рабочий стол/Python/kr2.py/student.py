from typing import Self
import random
import faker
class Student:
    def __init__(self, name:str, age: int, marks: tuple[int]):
        self.name, self.age, self.marks = name, age, marks
    def average_score(self)->float:
        return round(sum(self.marks)/len(self.marks),2) if self.marks else None
    @classmethod
    def create_random(cls)-> Self:
        marks = tuple([random.randint(0,4) for _ in range(random.randint)])
        return cls(faker.name(), random.randint(15,39), marks)
    def __gt__(self, other: Self)->bool:
        return self.average_score()>other.average_score()
    def __lt__(self, other: Self)->bool:
        return self.average_score()<other.average_score()
    def __ge__(self, other: Self)->bool:
        return self.average_score()>=other.average_score()
    def __lt__(self, other: Self)->bool:
        return self.average_score()<=other.average_score()
    def __eq__(self, other: Self)->bool:
        return self.average_score()==other.average_score()
    def __ne__(self, other: Self)->bool:
        return self.average_score()!=sother.average_score()
    @classmethod
    def create_random(cls)->Self:
        marks = [random.randint(0,4) for _ in range(random.randint(3,5))]
        if random.randint(0,100)<5:
            marks.append(5)
        faker_object = Faker()
        return cls(faker_object.name(), random.randint(15,39), tuple(marks))
    students = [Student.create_random() for _ in range(5 )]
