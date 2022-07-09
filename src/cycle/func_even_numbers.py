def even_numbers(start_number, end_number):
    return [number for number in range(int(start_number), int(end_number + 1)) if number % 2 == 0]

print(even_numbers(3, 7))