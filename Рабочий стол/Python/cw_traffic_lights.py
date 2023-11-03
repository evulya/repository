def update_light(current):
    lights = ['green', 'yellow','red']
    if current != lights[2]:
        return lights[lights.index(current)+1]
    else:
        return 'green'
print(update_light('green'))
print(update_light('red'))