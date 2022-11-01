from random import*
a = [randint(1,30) for i in range(10)]
b = [randint(1,30) for i in range(10)]
c = []
print(a)
print(b)
c = a
a = b
b = c
print(a)
print(b)
