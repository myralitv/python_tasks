def sum_of_numbers(user_numbers: tuple[:int]) -> int:
    for i in user_numbers:
        if not isinstance(i, (int, float)):
            raise TypeError(f'Argument "number" must be integer, not {type(i)}')

    sum_numbers = 0
    for i in user_numbers:
        sum_numbers += i
    return sum_numbers
