def even_elements(numbers: tuple[:int, :float]) -> list:
    for i in numbers:
        if not isinstance(i, (int, float)):
            raise TypeError(f'Argument "number" must be integer, not {type(i)}')

    return [number for number in numbers if number % 2 == 0]
