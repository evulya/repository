from sys import getsizeof
nums = [i for i in range(10**9)]
memory = sum([getsizeof(nums) + sum([getsizeof(item) for item in nums])])
print('Размер списка nums: {0}'.format[getsizeof(nums)])
range_ten_mill = range(10**7)
print('Размер генератора: {0}')
from typing import Generator
def range_(end: int, start:int =0,step: int =1)-> Generator:
    while step >0 and start < end or step < 0 and start>end:
        yield start 
        start += step 
for i in range_(10):
    if i==7:
        break
for i in range_ten:
    if i>7:
        range_ten.throw(Exeption('Генератор выдает значение больше 7'))
    print(i)
#fibonacci
def fibonacci()->Generator:
    fst,snd=0,1
    yield fst
    while True:
        yield snd
        fst, snd = snd, fst+snd
for index, value in enumerate(fibonacci):
    print(f'Фибоначчи {index} равен {value}')
    if index ==10:
        break
def half_life(years:float)->Generator:
    start, time = 1, years
    while True:
        yield start, time
        start /=2
        time +=years
i=0
for amount, years in half_life(1000):
    if i ==10:
        break
    print(f'Через {years} лет останется {amount*100} вещества')
    i+=1
    from datetime import date
    #generator leap years
    #если делится на 4 без остатка, а на 100 только с остатком - високосный, или делится без остатка на 400, в другом случае - невисокосный
def leap_years()-> Generator:
    year = date.today().year
    while year %4 != 0 and(year % 100 ==0 or year %400!=0):
        year +=1
    while True:
        if year %100 !=0 or year%400==0:
            yield year
        year +=4
i=0
for year in leap_years():
    if i > 20:
        break
    print(year)
    i+=1
from typing import Callable
def info(func: Callable):
    def new(*args, **kwargs):
        print(f'Running function {func.__name__}')
        print(f'Positional arguments: {args}')
        print(f'Keyword arguments: {kwargs}')
        result = func(*args, **kwargs)
        print(f'Result of {func.__name__}: {result}')
from time import time
def get_time(func: Callable)->Callable:
    def new(*args, **kwargs):
        start= time()
        result =func(*args,**kwargs)
        print(f'Функция {func.__name__} была выполнена за {time() - start} сек.')
        return result
    return 
timed_sum_two= get_time(sum_two)
print(timed_sum_two(2,2))
def calm_the_text(text:str)->str:
    return text.lower().replace('!', '.')
print(calm_the_text(''))
def work_with_text(text:str)->str:
    return text.lower().replace('!', '.')
print(calm_the_text)
#декораторб заставляющий функцию возвращать квадрат результатов
def square(func: Callable)-> Callable:
    return (lamda x: func(x)**2)
@square
def sum_two(a,b):
    return a+b
print(sum_two(1,1))

#декораторы генераторов
def enum_my_generator(gen_func: Callable)-> Callable:
    def new(*args, **kwargs)-> Generator:
        index = 0
        for value in gen_func(*args, **kwargs):
            yield index, value
            index += 1
            return new