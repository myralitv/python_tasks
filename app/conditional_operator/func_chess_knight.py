def chess_knight(x1: int, y1: int, x2: int, y2: int) -> str:
    range_number = range(1, 9)
    if not isinstance(x1, int):
        raise TypeError(f'Argument "x1" must be integer, not {type(x1)}')
    if not isinstance(y1, int):
        raise TypeError(f'Argument "y1" must be integer, not {type(y1)}')
    if not isinstance(x2, int):
        raise TypeError(f'Argument "x2" must be integer, not {type(x2)}')
    if not isinstance(y2, int):
        raise TypeError(f'Argument "y1" must be integer, not {type(y2)}')
    if x1 not in range_number:
        raise ValueError(f'Argument "x1":{x1} must be greater than 0 and less than 9')
    if y1 not in range_number:
        raise ValueError(f'Argument "y1":{y1} must be greater than 0 and less than 9')
    if x2 not in range_number:
        raise ValueError(f'Argument "x2":{x2} must be greater than 0 and less than 9')
    if y2 not in range_number:
        raise ValueError(f'Argument "y2":{y2} must be greater than 0 and less than 9')

    if (x1 == x2-1 or x1 == x2+1) and (y1 == y2-2 or y1 == y2+2) and x1 != x2 and y1 != y2:
        return "Yes"
    elif (x1 == x2-2 or x1 == x2+2) and (y1 == y2-1 or y1 == y2+1) and x1 != x2 and y1 != y2:
        return "Yes"
    else:
        return "No"
