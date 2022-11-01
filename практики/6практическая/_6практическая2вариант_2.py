from random import*
a = [randint(-50,50)for i in range(15)]
b = []
c = []
print(a)
for i in range(len(a)):
    if a[i]>0:
        b.append(a[i])
    else:
        c.append(a[i])
print(b)
print(c)