

def is_prime(a):
    def wrapper(*args, **kwargs):
        n = a(*args, **kwargs)
        if n == 0:
            print('Ноль')
            return n
        elif n == 1 or -1:
            print('Простое')
            return n
        is_prostoe = 1
        for k in range(2, n):
            if n % k == 0:
                print('Составное')
                is_prostoe = 0
                break
        if is_prostoe == 1:
            print('Простое')
        return n
    return wrapper

@is_prime
def sum_three(a: float, b: float, c: float):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)