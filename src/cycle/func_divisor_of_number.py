def divisor_of_number(number):
    return [divisor for divisor in range(1, number + 1) if number % divisor == 0]

print(divisor_of_number(25))