import pytest
from string import ascii_lowercase

import main


count_vowels_data = [('aui', 3), ('sdfgh', 0), ('abcdef', 2), ('', 0)]

@pytest.mark.parametrize('text, expected', count_vowels_data)
def test_count_vowels(text: str, expected: int):
    assert main.count_vowels(text) == expected
    assert main.short_count_vowels(text) == expected


contains_all = 'the quick brown fox jumps over the lazy dog'
all_letters_data = [(contains_all, True), (ascii_lowercase, True), ('', False), ('askdb', False)]

@pytest.mark.parametrize('text, expected', all_letters_data)
def test_all_letters(text: str, expected: bool):
    assert main.contains_all_letters(text) == expected

missing_letters_data = [(ascii_lowercase.replace(symbol, ''), [symbol]) for symbol in ascii_lowercase]

@pytest.mark.parametrize('text, expected', missing_letters_data)
def test_missing_letters(text: str, expected: bool):
    assert main.get_missing_letters(text) == expected
