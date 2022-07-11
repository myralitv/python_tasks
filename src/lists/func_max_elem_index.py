def max_index_elements(numbers: tuple[:int, :float]) -> tuple:
    for i in numbers:
        if not isinstance(i, (int, float)):
            raise TypeError(f'Argument "number" must be integer, not {type(i)}')

    return max(numbers), numbers.index(max(numbers))


print(max_index_elements((5, 10, 6, 11, 3, 8, 9, 7)))