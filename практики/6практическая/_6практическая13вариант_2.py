from random import *
a = [randint(1,20) for i in range(8)]
print(a)
for i in range(len(a)):
    if a[i]<15:
        a[i]=a[i]*2
print(a)
