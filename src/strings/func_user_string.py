def user_string(string: str) -> tuple[:str, :int]:
    if not isinstance(string, str):
        raise TypeError(f'Argument "word" must be string, not {type(string)}')
    if len(string) < 5:
        raise ValueError(f'Argument "string" must be greater than or equal to 5')
    return string[2], string[-2], string[:5], string[0:-2], string[::2], string[1::2], string[::-1], len(string)


print(user_string('welcome'))