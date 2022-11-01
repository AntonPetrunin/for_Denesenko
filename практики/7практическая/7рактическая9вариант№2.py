from random import*
n = int(input())
a = [randint(1,100)for i in range(n)]
b = [randint(1,100)for j in range(n)]
c = [randint(1,100)for g in range(n)]
print(a)
print(b)
print(c)
def s(x):
    p = 1
    s = 0
    for i in range(len(x)):
        p*=x[i]
        s+=x[i]
    print(p)
    print(s/n)
s(a)
s(b)
s(c)