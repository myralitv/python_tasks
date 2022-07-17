def sort_number(numbers: list[:int, :float]) -> list:
    for i in numbers:
        if not isinstance(i, (int, float)):
            raise TypeError(f'Argument "number" must be integer, not {type(i)}')

    return sorted(numbers)

