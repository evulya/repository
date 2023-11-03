def fake_bin(x):
    numbers = ''
    for i in x:
        i = int(i)
        if i<5:
            numbers = numbers + '0'
        else:
            numbers = numbers + '1'
    return numbers
print(fake_bin('45385593107843568'))