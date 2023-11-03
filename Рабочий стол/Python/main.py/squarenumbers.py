from typing import List
def square_even(numbers)List(int) -> List(int):
    result = []
    for number in numbers:
        if number %2 ==0:
            result.append(number**2)
        else:
            result.append(number)
    return result
if __name__ =='__main__':
    print(square_even(num for num in range(0,10)))
