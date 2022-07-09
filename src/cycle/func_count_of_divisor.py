def count_divisor(number):
    return len([divisor for divisor in range(1, number + 1) if number % divisor == 0])

print(count_divisor(25))