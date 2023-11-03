def count_vowels(text: str)->int:
    vowels='aeuioy'
    counter= 0 
    for symbol in text.lower():
        if symbol in vowels:
            counter+=1
    return counter
print(count_vowels('quick red fox jumps over lazy dog'))

def short_count_vowels(text: str) ->int:
    vowels = 'aeuioy'
    text = text.lower()
    return sum([text.count(symbol)  for symbol in vowels])

def get_missing_letters(text: str)->list:
    from string import ascii_lowercase
    text = text.lower()

def top_ten_words(text:str)-> None:
    from string import punctuation
    text=text.lower().replace('/n', '')
    for symbol in punctuation + '-':
        text = text.replace(symbol, ' ')
    print(punctuation)

"""module for calculating different types of salaries"""
"""calculate hourly salary based on actual hours and position in company.

Args
    position: str - position in company.
    hours: int - actual hours.
    
Returns:
    tuple of two floats: salary after tax, tax itself.
"""
TAX = 0.13
from typing import NamedTuple
def hour_salary(position: str, hours: float)-> tuple[float]:
    #used constants
    rates= {'Junior': 70000, 'Middle': 120000, 'Senior': 180000}
    rate = rates.get(position)
    if not rate:
        raise Exception(f'Position <{position}> is not defined in rates.')
    normal_hours = 160
    # check if position defined in rates
    # calculation
    half=rate/2
    pretax = half+ half*(hours/normal_hours)
    after_tax = round(pretax * (1-TAX), 2)
    return pretax - after_tax #salary after tax and tax itself

def coach_salary(trainings: tuple[int])->tuple[float]:
    """ Calculate salary based on trainings number,
    
    Args: 
        trainings: - tuple of int, each number refferes to number of people.
    Returns:
        tuple of two floats: salary after tax, tax itself"""
    rate = 150
    pretax= sum(trainings)*rate
    after_tax= round(pretax*(1-TAX),2)
    return after_tax,pretax - after_tax