def get_matrix(n, m, value):
    matrix = []
    for row in range(n):
        Buzz = []
        matrix.append(Buzz)
        for column in range(m):
            Buzz.append(value)
    return matrix
print(get_matrix(3,5,'Я сделал'))



JK = get_matrix(3, 3, 'Элитарно')
print('[')
for n in JK:
    print('   ', n)
print(']')
