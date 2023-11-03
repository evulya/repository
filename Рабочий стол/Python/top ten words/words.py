from string import punctuation

def clean(text: str) -> str:
    """Clean the text from punctuation marks and newline character.

    Args:
        text: str - a text to be cleansed.

    Returns:
        str - a cleansed text.
    """
    text = text.lower().replace('\n', ' ')
    for symbol in f'{punctuation}–':
        text = text.replace(symbol, ' ')
    return text

with open('source.txt', 'r') as file:
    text = clean(file.read())

words = text.split()

while True:
    letter = input('Введите букву: ')
    print([word for word in words if word.startswith(letter)])