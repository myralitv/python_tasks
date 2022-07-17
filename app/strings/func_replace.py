def func_replace(string: str) -> str:
    if not isinstance(string, str):
        raise TypeError(f'Argument "word" must be string, not {type(string)}')
    if string.count('1') < 1:
        raise ValueError(f'Argument "string":{string} must be greater than or equal to 1')

    return string.replace('1', 'one')
