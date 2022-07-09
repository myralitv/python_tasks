def user_string(string):
    return string[2], string[-2], string[:5], string[0:-2], string[::2], string[1::2], string[::-1], len(string)

print(user_string('winterborn'))