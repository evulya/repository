def digitize(n):
    list_numbers =[]
    n = str(n).split()
    n = ''.join(n)
    for number in n:
        list_numbers.append(int(number))
    return list_numbers[::-1]
print(digitize(35231))
    
