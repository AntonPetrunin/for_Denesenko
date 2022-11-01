from random import *
m = 0
a = [randint(1,100) for i in range(10)]
print(a)
for i in range(len(a)):
    m = max(a[i],m)
print(a.index(m)+1)
print(m)


