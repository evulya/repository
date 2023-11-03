#счетчик Counter
from time import time
class Counter:
    def __init__(self):
        self.__value =0
    @property
    def value(self)-> int:
        return self.__value
    def increment(self)-> None:
        self.__value+=1
    def reset(self)-> None:
        self.__value = 0
my_counter = Counter()
print('First stage of a game')
for _ in range(10):
    time.sleep(1)
    my_counter.increment()
    print(my_counter.value)
    print('second stage of a game')
    my_counter.reset()
for _ in range(10):
    time.sleep(1)
    my_counter.increment()
    print(my_counter.value)
my_counter.increment()
print(my_counter._value)