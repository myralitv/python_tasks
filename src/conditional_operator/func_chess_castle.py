def chess_castle(x1: int, y1: int, x2: int, y2: int) -> str:
    if not isinstance(x1, int):
        raise TypeError(f'Argument "x1" must be integer, not {type(x1)}')
    if not isinstance(y1, int):
        raise TypeError(f'Argument "y1" must be integer, not {type(y1)}')
    if not isinstance(x2, int):
        raise TypeError(f'Argument "x2" must be integer, not {type(x2)}')
    if not isinstance(y2, int):
        raise TypeError(f'Argument "y1" must be integer, not {type(y2)}')
    if x1 < 0:
        raise ValueError(f'Argument "x1":{x1} must be greater than 0')
    if y1 < 0:
        raise ValueError(f'Argument "y1":{y1} must be greater than 0')
    if x2 < 0:
        raise ValueError(f'Argument "x2":{x2} must be greater than 0')
    if y2 < 0:
        raise ValueError(f'Argument "y2":{y2} must be greater than 0')

    if (x1 == x2 or y1 == y2) and (0 < x1 <= 8 and 0 < y1 <= 8 and 0 < x2 <= 8 and 0 < y2 <= 8):
        return "Yes"
    else:
        return "No"


print(chess_castle(8, 4, 5, 4))

# def chess_castle(x1, y1, x2, y2):
#     if x1 == x2 or y1 == y2:
#         return "Yes"
#     else:
#         return "No"
