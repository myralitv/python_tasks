def unique_element(numbers: list[:int, :float]) -> list:
    for i in numbers:
        if not isinstance(i, (int, float)):
            raise TypeError(f'Argument "number" must be integer, not {type(i)}')
    dictionary_of_elements = {}
    list_of_unique = []
    for element in numbers:
        if element in dictionary_of_elements:
            dictionary_of_elements[element] += 1
        else:
            dictionary_of_elements[element] = 1

    for key, value in dictionary_of_elements.items():
        if value == 1:
            list_of_unique.append(key)
    return list_of_unique

