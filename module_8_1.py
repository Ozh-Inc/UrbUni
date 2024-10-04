def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        return str(a) + str(b)

print(add_everything_up(18, 'peacock'))
print(add_everything_up(145.17, 'BUZZ'))
print(add_everything_up(19, 488.95))