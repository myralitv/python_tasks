def leap_year(year: int):
    if year % 4 == 0:
        return "Yes"
    elif year % 100 == 0:
        return "No"
    elif year % 400 == 0:
        return "Yes"
    else:
        return "No"


print(leap_year(2020))