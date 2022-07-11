def zero_in_list(numbers: tuple[:int, :float]) -> str:
    for i in numbers:
        if not isinstance(i, (int, float)):
            raise TypeError(f'Argument "number" must be integer, not {type(i)}')
    if 0 in numbers:
        return 'Yes'
    else:
        return 'No'


print(zero_in_list((6, 5.5, 5, 0)))