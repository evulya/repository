#вывод всех чисел от N до 0
def to_zero(number: int)-> None:
    """Prints all numbers from number to zero"""
    print(number)
    if number != 0:
        to_zero(number - 1 if number > 0 else number - 1)
to_zero(-4)