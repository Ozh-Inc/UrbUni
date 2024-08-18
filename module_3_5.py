def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) == 1:
        return first
    if '0' in str_number:
        return 0
    return first * get_multiplied_digits(int(str_number[1:]))


print(get_multiplied_digits(5))
print(get_multiplied_digits(567934701))
print(get_multiplied_digits(38245676834))
