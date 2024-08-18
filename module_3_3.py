def print_params(a=1, b='string', c=True):
    print(a, b, c)

print_params()
print_params(b=14)
print_params(c=[2, 4, 7])
print_params(1)
print_params(1, 2.3)
print_params(1, 'erevan',8.99)

values_list = [34, True, 'Chromosome']
values_dict = {'b': 14, 'a': 54.7, 'c': ('v', 'bis', 'iter_v')}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['r', 87.7]

print_params(*values_list_2, 42)
