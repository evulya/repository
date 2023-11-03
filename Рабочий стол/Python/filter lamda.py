def f(x): return x
y = 1
f = lamda x: (x, y)
print(type(f))
#without arguments
def agree(): return True
agree= lamda: True
# returns multiple arguments
def f(x): return x, x **2
f = lamda x: (x, x **2) # скобки обязательны
# dot -> (x, y)
def sum_dots(dot_1: tuple, dot_2: tuple)-> tuple:
    return dot_1[0] + dot_2[0], dot_1[1] + dot_2[1]
# takes and returns multiple arguments
sum_dots = lamda dot_1, dot_2: (dot_1[0] + dot_2[0], dot_1[1] + dot_2[1])
# all args
def return_args(*args, *kwargs):
    return args, kwargs
return_args = lamda *args, **kwargs: (args, kwargs)
#sorted по длине
def get_len(word:str) -> int:
    return len(word)
words = ['python', 'is', 'great']
#1
print(sorted(words, key = get_len))
#2
print(sorted(words, key =lamda word: len(word)))
#3
print(sorted(words, key= len))
#filter в списке оставить слова, в которых есть гласные
words = ['python', 'lkm', 'great', ' ltrnk']
vowels = 'aeuioy'
def has_vowels(words: str)->bool:
    return any(vowel in word for vowel in vowels)
#1 comrehention 
print(word for word in words if has_vowels(word))
#2 filter
print(list(filter(has_vowels, words)))
#3 filter lamda
print(list(filter(lamda word)))
def square (x:int(float))-> int|float:
    return x**2
nums = [1, 2, 3]
#1 comrehention (включение)
print(num ** 2 for num in nums)
#2 map
print(list(map(square, nums))): # через цикл можно без приведения к списку
    print(num)
#3 map lamda
print(list(map(mada x: x ** 2, nums)))
# принимаем словарь с товаром и их кол-вом продаж
# возвращаем топ-3 iphone по кол-ву продаж, только их названия
sales = {
    'нормальная парта': 0,
    'iphone 3 ': 2,
    'iphone 15': 150,
}
def top_iphones(sales: dict) -> Tuple[str]:
    def is_phone(good: tuple) -> bool:
        return good[0].lower().startswith('iphone')
    iphones = list(filter(lamda good))