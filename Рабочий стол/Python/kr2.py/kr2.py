#2 
def summ(a):
    while True:
        try:
            a = list(int(input('Введите числа: ')))  
        except Exception:
            print('Вы ввели не число')
        else:
            if a == 'q':
                print(f'Сумма чисел {a} равна {sum(a)}')
                break
    return f'Сумма чисел {a} равна {sum(a)}'
#3
def dictionary(a: dict, b: dict, c:str = 'a')->dict:
    two_dict = a.update(b)
    second_dict={}
    for i in two_dict.keys():
        if c in i:
            two_dict[i] = second_dict[i]
    return second_dict
dictionary({'a': 1, 'b': 2}, {'c':3, 'd': 4})
from typing import Generator
#4
def numbers(N: int, a = True)-> Generator:
    b= []
    if a:
        for i in range(0,N,2):
            b.append(i)
    else:
        for j in range(1, N, 2):
            b.append(j)
    yield b
numbers(2)
#5
def decorator(func):
    def new_func(*args, **kwargs):
        for arg in args:
            try:
                arg.isinstance(float, int)
            except ValueError:
                print('Value Error')
            else: 
                result = new_func(*args, **kwargs)
                return result
@decorator
def some_func(a,b):
    return a+b
# some_func(1,2)
                
        
