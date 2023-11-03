#вывод всех элементов списка
def print_values(values: list)->None:
    """Prints all values in a list recursively"""
    if values:
        print(values.pop(0))
        print_values(values)
print_values([7,12,1987])
#список всех цифр целого числа
def all_digits(number:int)->list[int]:
    if number<10:
        return [number]
    last_digit =number%10
    return all_digits(number//10)+ [last_digit]
print(all_digits(12345))