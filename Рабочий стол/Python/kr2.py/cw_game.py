def points(games):
    count = 0
    count2 =0
    for res in games:
        x= int(res[0])
        y= int(res[2])
    while count2 <=10:
        if x>y:
            count+=3
        elif x==y:
            count+=1
        else:
            continue
        count2 +=1
    return count
print(points(['1:1', '2:1', '3:1', '1:2']))

