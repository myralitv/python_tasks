def count_divisor(number: int) -> int:
    if not isinstance(number, int):
        raise TypeError(f'Argument "number" must be integer, not {type(number)}')
    if number < 0:
        raise ValueError(f'Argument "number":{number} must be greater than 0')

    return len([divisor for divisor in range(1, number + 1) if number % divisor == 0])


print(count_divisor(42))