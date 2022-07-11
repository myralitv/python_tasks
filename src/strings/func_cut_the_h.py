def cut_h(word: str) -> str:
    if not isinstance(word, str):
        raise TypeError(f'Argument "word" must be string, not {type(word)}')
    if word.count('h') < 2:
        raise ValueError(f'Argument "h" in word: {word} must be greater than or equal to 2')

    remove_word = 'h'
    return word[:word.index(remove_word)] + word[word.rindex(remove_word) + 1:]

print(cut_h('welh1234567890hcome'))

