from random import*
n = int(input())
a = [randint(1,30)for i in range(n)]
k = 0
print(a)
for i in range(len(a)):
    if a[i]>k and a[i]%2==0:
        k = a[i]
print(k)