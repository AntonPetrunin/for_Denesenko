from random import*
a=[randint(1,35)for i in range(15)]
print(a)
for i in range(len(a)):
    if a[i] < 10:
        a[i]=0
    if a[i]>20:
        a[i]=1
print(a)