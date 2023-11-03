def no_space(x: str)->str:
    if ' ' in x:
        x2 = x.replace(' ', '')
        return x2
    else:
        return x
print(no_space('jvfj vfj    vvfnvj  jdn  kknnvc'))