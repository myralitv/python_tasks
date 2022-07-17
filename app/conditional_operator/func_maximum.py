def maximum(x: int, y: int) -> int:
    if not isinstance(x, int):
        raise TypeError(f'Argument "x" must be integer, not {type(x)}')
    if not isinstance(y, int):
        raise TypeError(f'Argument "y" must be integer, not {type(y)}')
    return max(x, y)
