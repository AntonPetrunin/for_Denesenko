from random import*
a = [randint(1,30)for i in range(10)]
k = 1000000000000
print(a)
for i in range(len(a)):
    if a[i]%2==1 and a[i]<k:
        k = a[i]
print(k)




