def is_isogram(string:str):
    amount_l = [list(string.lower()).count(letter.lower()) for letter in string] 
    amount_l.sort(reverse=True)
    if string == '':
        return True
    else:
        for n in amount_l:
            if n>1:
                return False
            else:
                return True
print(is_isogram('Dermatoglyphics'))
print(is_isogram(''))
print(is_isogram('moOse'))