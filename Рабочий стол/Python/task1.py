def slovar(slov: {str: int|float}) -> dict:
    result={}
    for num1, num2 in slov.items():
        if num2 %2 == 0:
            result[num1] = num2
    return result
slovar({1:2,2:3, 3:4, 4:5})


def index_list(list1: list):
    ind= int(input('Введите индекс: '))
    return list1[ind]
print(index_list([1, 2, 3]))


# def index_str(list_str: list(str), str1: str)-> int:
#     d = {}
#     amount = list_str.count(str1)
#     for i in list_str
        
#     return index(list_str)

from typing import Generator

def val(N: int)->Generator:
    def generator():
        for i in range(0, N, 1):
            print(i)
        return generator()
print(val(1))

def val(N:int)->Generator:
    def val2():
        for num in range(0, N):
            print(num)
            num += 1
    yield val2()
print(val(1))

def dec(func):
    def func2(*args, **kwargs):
        return args, kwargs
@dec
def func3(a = 1):
    c = a+b
    return c
print(func3())

     
    

    
        