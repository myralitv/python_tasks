def count_words(word: str) -> int:
    if not isinstance(word, str):
        raise TypeError(f'Argument "word" must be string, not {type(word)}')

    return len(word.split())


print(count_words('gd54'))