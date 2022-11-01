from random import*
a = [randint(1,7)for i in range(9)]
b = []
print(a)
for i in range(len(a)):
    if a.count(a[i])>1:
        b.append(a[i])
b= list(set(b))
print(b)

