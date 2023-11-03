def filter_list(l):
    l2 =[]
    for item in l:
        if isinstance(item, int):
            l2.append(item)
        else:
            continue
    return l2
print(filter_list([1, 2, 'str', 4]))
                
                
            
