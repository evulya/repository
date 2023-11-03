def binary_array_to_number(arr:list):
    arr = arr[::-1]
    count=0
    list=[]
    for number in range(len(arr)+1):
        list.append(number)
    for num1, num2 in zip(list, arr):
        n=num2*(2**num1)
        count+=n
    return count
print(binary_array_to_number([1, 0, 1, 1]))
