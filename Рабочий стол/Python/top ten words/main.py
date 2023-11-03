from string import ascii_lowercase


def count_vowels(text: str) -> int:
    vowels = 'aeuioy'
    counter = 0
    for symbol in text.lower():
        if symbol in vowels:
            counter += 1
    return counter

def short_count_vowels(text: str) -> int:
    vowels = 'aeuioy'
    text = text.lower()
    return sum([text.count(symbol) for symbol in vowels])

def contains_all_letters(text: str) -> bool:
    repeat_letters = set(ascii_lowercase) & set(text.lower())
    return len(repeat_letters) == len(ascii_lowercase)

def get_missing_letters(text: str) -> list:
    text = text.lower()
    return [symbol for symbol in ascii_lowercase if symbol not in text]

magic_string = 'the quick brown fox jumps over the lazy dog'
print(get_missing_letters(magic_string))