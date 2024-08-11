numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
PROSTOE = []
SOSTAVNOE = []
for n in numbers:
    if n == 1:
        continue
    is_prostoe = 1
    for k in range(2, n):
        if n % k == 0:
            SOSTAVNOE.append(n)
            is_prostoe = 0
            break
    if is_prostoe == 1:
        PROSTOE.append(n)
print(PROSTOE, SOSTAVNOE)
