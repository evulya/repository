def basic_op(operator, value1, value2):
    if operator == '+':
        return value1+value2
    elif operator =='-':
        return value1-value2
    elif operator =='*':
        return value1*value2
    elif operator =='/':
        return value1/value2
    else:
        return 'нет оператора'
print(basic_op('+', 4, 7))