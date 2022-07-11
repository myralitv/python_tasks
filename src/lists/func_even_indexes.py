def even_indexes(numbers: tuple[:int, :float]) -> list:
    for i in numbers:
        if not isinstance(i, (int, float)):
            raise TypeError(f'Argument "number" must be integer, not {type(i)}')

    return [number for number in numbers if numbers.index(number) % 2 == 0]


print(even_indexes(('3', 10, 6, 11, 3, 8, 9, 7)))