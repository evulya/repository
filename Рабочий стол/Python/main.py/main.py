from salary import hourly_salary
exit_='q'
exit_msg = f'[{exit_} to quit]'
position = input('Type down position')
hours = input('Actual hours: ')
while True:
    position = input(f'Type down position{exit_msg}:')
    if position == exit_:
        break
    try:
    hours = float(hours)
except ValueError:
    print('Value is not a number or decimal point is not a dot.')
    try:
        salary, tax = hourly_salary(position, hours)
    except Exception as error:
        print(error)
else:
    print(f'After tax salary: {salary}')
    print(f'Tax:')
