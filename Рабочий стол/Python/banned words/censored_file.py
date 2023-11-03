from typing import List
def get_word_case_mutations(word: str) -> List[str]:
    def fill_zeros(text:str) -> str:
        filler = (len(word)-len(text)) * '0'
        return filler + text
    word = word.lower()
    result =[]
    for i in range(2**len(word)):
        bits = fill_zeros(bin(i)[2:])
        new=''.join(char.upper() if bit == '1' else char for char, bit in zip(word,bits))
        result.append(new)
    return result
    current = [] 
def censor_the_file(source_file: str, banned: str='banned_text.txt'):
    with open(banned_words) as banned:
        lines = banned.readline()
words = [word.replace('\n', '') for word in lines]
with open(source_file) as source:
    text = source.read()
for word in words:
    filler = '*'*len(word)
    text = text.replace(word, filler)
with open(f'censored_{source_file}', 'w') as output:
    output.write(text)
if __name__ == '__main__':
    censor_the_file('file.txt')
