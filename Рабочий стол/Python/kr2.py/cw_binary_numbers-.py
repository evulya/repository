def add_binary(a,b):
    c = a+b
    number = []
    while c:
        number.append(str(c%2))
        c //= 2
        number.reverse()
    number = ''.join(number)
    return number
print(add_binary(57, 21))