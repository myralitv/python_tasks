def zero_in_list(numbers):
    if 0 in numbers:
        return 'Yes'
    else:
        return 'No'

print(zero_in_list([3, 5, 10, 0]))