def square(func: Callable)-> Callable:
    return (lamda x: func(x)**2)
@square
def sum_two(a,b):
    return a+b
print(sum_two(1,1))
