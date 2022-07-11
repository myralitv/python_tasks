def leap_year(year: int) -> str:
    if not isinstance(year, int):
        raise TypeError(f'Argument "year" must be integer, not {type(year)}')
    if year < 0:
        raise ValueError(f'Argument "year":{year} must be greater than 0')

    if year % 4 == 0:
        return "Yes"
    elif year % 100 == 0:
        return "No"
    elif year % 400 == 0:
        return "Yes"
    else:
        return "No"


print(leap_year(2024))