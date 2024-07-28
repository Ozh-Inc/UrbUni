# 1st program
print(9 ** 0.5 * 5)
# 2nd program
print(9.99 > 9.98 and 1000 != 1000.1)
# 3rd program
a = 1234
b = 5678
a = str(a)
b = str(b)
a = a[1:-1]
b = b[1:-1]
a = int(a)
b = int(b)
print(a + b)
# 4th program Experimental
a = 13.42
b = 42.13
a1 = int(a)
b1 = int(b)
aX = str( round(a - a1, 2) )
aX = aX[2:]
bX = str( round(b - b1, 2) )
bX = bX[2:]
# Debug: print(aX, bX)
# Debug: print( round(a - a1, 2) )
print( a1 == int(bX) or b1 == int(aX) ) # Интересный эксперимент. Очень интересный.
# 4th program Final Ver.
a = 13.42
b = 42.13
a1 = int(a)
b1 = int(b)
print( a1 == int((b - b1) * 100) or b1 == int((a - a1) * 100) )
