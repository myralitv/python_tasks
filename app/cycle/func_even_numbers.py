def even_numbers(start_number: int, end_number: int) -> list:
    if not isinstance(start_number, int):
        raise TypeError(f'Argument "number" must be integer, not {type(start_number)}')
    if not isinstance(end_number, int):
        raise TypeError(f'Argument "number" must be integer, not {type(end_number)}')
    if start_number > end_number:
        raise ValueError(f'Argument "start_number"{start_number} must be biggest than "end_number"{end_number}')

    return [number for number in range(int(start_number), int(end_number + 1)) if number % 2 == 0]
