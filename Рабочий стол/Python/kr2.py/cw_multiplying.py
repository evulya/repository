def grow(arr: list[int|float])->int|float:
    result = 1
    for number in arr:
        result *= number
    return result
print(grow([1, 2, 3, 4]))

