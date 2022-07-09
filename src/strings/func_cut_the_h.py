def cut_h(word: str) -> str:
    remove_word = 'h'
    return word[:word.index(remove_word)] + word[word.rindex(remove_word) + 1:]

print(cut_h('1234hmvekh567890'))

