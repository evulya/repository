# 1
# объявить два списка, заполнить циклом
# один - значениями всех четных чисел в отрезке [-10; 10]
# второй - значениями всех нечетных чисел в отрезке [-10, 10]

odd_num = list()
eien_num = list()
for i in range(-9, 11, 2):
    odd_num.append(i)
for n in range(-10, 11, 2):
    eien_num.append(n)
print(odd_num, eien_num)

# 2
# выполнить задание 1 включением
odd_num = [i for i in range(-9, 11, 2)]
eien_num = [n for n in range(-10, 11, 2)]
print(odd_num, eien_num)

# 3
# объявить словарь, заполнить циклом.
# ключи - числа отрезка [-20; 20],
# при этом значения словаря: 
# для чисел >= 0  - их корень,
# для чисел < 0   - сообщение 'ошибка, корень отрицательного числа'
squares = dict()

for number in range(-20, 21):
    squares[number] = 'ошибка' if number < 0 else number ** 0.5

print(squares) 

# 4
# выполнить задание 3 включением

a = {key:round((key ** .5), 2) if key>=0 else 'ошибка' for key in range(-20,21)}
print(a)

# 5
# объединить списки из задания 1 в отсортированном виде по возрастанию
# так, чтобы получился список всех чисел от 10 до -10
result = odd_num + eien_num
print(sorted(result)[::-1])
print(list(reversed(sorted(result))))
print(sorted(result, reverse=True))

# 6
# оставить в словаре (3) только те пары, в которых значение - число (float, int)
b = {}
for key in a:
    if isinstance(a[key], (int, float)):
        b[key] = a[key]
print(b)

a = {key: a[key] for key in a if isinstance(a[key], (int, float))}
print(a)

# 7
# удвоить все значения словаря, в которых есть цифра 2

for key in a:
    if "2" in str(a[key]):
        a[key] = a[key] * 2
print(a)
# 8
# написать защищенную от ошибок программу,
# которая от пользователя с клавиатуры получает число, а возвращает квадрат
# try:
#     num = int(input('Enter your number: '))
# except:
#     print('Error')
# else:

#     print(f'Square: {num ** 2}')

# 9
# написать функцию, которая принимает два словаря, а возвращает их объединение
def merge_two_dict(a: dict, b: dict) -> dict:
    a.update(b)
    return a
print(merge_two_dict({1: 1, 2: 4}, {2: 3}))

# 10
# написать функцию, которая принимает строку и проверяет, что это адрес почты
# считать, что это почта, если в строке нет пробелов 
# и она заканчивается на @сервер, где сервер - что-то из списка
# ['yandex.ru', 'mail.ru']

def pochta(text: str) -> bool: 
    servers = ['@yandex.ru', '@mail.ru']
    return text.endswith(servers[0]) or text.endswith(servers[1]) and not " " in text
print(pochta("michailsobakamail.ru"))

# 11
# написать функцию, которая принимает словарь, и возвращает
# Truе, если значения в словаре повторяются, а иначе False

def slovar(s: dict) -> bool:
    return len(s.values()) > len(set(s.values()))
print(slovar({1: 1, 2: 2})) 

# 12
# написать функцию, которая принимает текст и список слов
# возвращает кол-во вхождений всех слов в текст
# (например, f('ae Ae bF Bf ea', ['ae', 'bf']) вернет 4)
def count_words(text: str, words: list) -> int:
    text = text.lower()
    count = 0
    for word in words:
        count += text.count(word.lower())
    return count
print(count_words('ae Ae bF Bf ea', ['ae', 'bf']))
    


# 13
# написать фукнцию, которая принимает любое кол-во позиционных и ключевых арг.
# выводит их количество, а также сами значения в след. виде:
# позиционные - строкой через пробел
# ключевые - в столбец, например
# a - 1
# b - 2

def func_return(*args,**kwargs):
    print(' '.join([str(el) for el in args]), f'Len args: {len(args)}')
    print(f'Len kwargs: {len(kwargs)}')
    for key, val in kwargs.items():
        print(f'{key} - {val}')


func_return(1, 2, 3, 4, 5, a=1, b=2)

# 14
# написать функцию, которая принимает любой итерируемый тип данных
# и число - кол-во элементов, которые она возьмёт из него случайным образом
# это число по умолчанию равно 1
# возвращает два значения: список этих элементов и число,
# которое является процентом (кол-во элементов относительно всей длины)
from typing import Iterable, Tuple
from random import randint, sample

def get_random_items(items: Iterable, count: int = 1) -> Tuple[list, float]:
    items = list(items)
    result_length = round((count / len(items)) * 100, 2)
    # result_items = list()

    # for _ in range(count):
    #     random_int = randint(0, len(items) - 1)
    #     result_items.append(items.pop(random_int))
    result_items = sample(items, count)
    return (result_items, result_length)
        
print(get_random_items((1, 2, 3, 4, 5), 3))

# 15
# написать генератор, который принимает число N
# и выдаёт четные числа от 0 до N включительно
# если дано отрицательное N, идёт от 0 в отрицательную сторону

from typing import Generator
# def koroche_my_func(n: int) -> Generator:
#     step = 1 if n >= 0 else -1
#     for number in range(0, n + step, 2 * step):
#         yield number

# for i in koroche_my_func(-5):
#     print(i)


# 16
# написать генератор, который принимает строку и число N 
# генератор выдаёт случайную строку из символов исходной строки N раз

from random import shuffle
def koroche_my_func_2(text: str, n: int) -> Generator:
    letters = list(text)
    for _ in range(n):
        shuffle(letters)
        yield ''.join(letters)

for i in koroche_my_func_2('abcdef', 3):
    print(i)

# 17
# написать декоратор, который будет засекать время выполнения функции
from typing import Callable
from time import time

def func_dec_time(func: Callable) ->  Callable:
    def new_function(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print(f'Time left: {time() - start}')
        return result
    return new_function

func_dec_test = func_dec_time(get_random_items)

print(func_dec_test((1, 2, 3, 4, 5), 3))

# 18
# написать функцию, сортирующую вложенный список по второму элементу
# использовать sort (или sorted) и лямбда-функцию
def function_sor(items: list) -> list:
    return sorted(items, key=lambda x: x[1])

print(function_sor([[1,2],[1,1]]))
# 19
# написать функцию, которая принимает текст вида 'a1bcd3ef'
# в тексте какие-то наборы букв разделены цифрами (не числами!)
# каждую цифру следует заменить на соответствующее кол-во пробелов
# например, 'a1bcd3ef' -> 'a bcd   ef'

def function_num(text: str) -> str:
    new_text = ''
    # for s in text:
    #     if s.isdigit():
    #         new_text += ' ' * int(s)
    #     else:
    #         new_text += s

    return ''.join([' ' * int(s) if s.isdigit() else s for s in text])

print(function_num('dj1k2w'))


