"""Counting words statistics in text files."""

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


def top_ten_words(text: str) -> None:
    """Count top-10 words in text.

    Args:
        text: str - source text to get stats from.
    """
    words = clean(text).split()
    stats = {word: words.count(word) for word in set(words) if word != 's'}
    top = sorted(stats.items(), key=lambda pair: pair[1], reverse=True)
    for word, num in top[:10]:
        print(f'{word}\t: {num}')


with open('colette_lorand.txt', 'r') as lorand_bio:
    top_ten_words(lorand_bio.read())
