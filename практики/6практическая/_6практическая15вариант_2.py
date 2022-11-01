from random import*
a = [randint(1,100)for i in range(10)]
b = []
print(a)
for i in range(len(a)):
    if a[i]%2==1:
        b.append(a[i])
b.reverse()
print(b)
