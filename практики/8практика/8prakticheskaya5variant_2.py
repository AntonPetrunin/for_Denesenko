from random import*
n = int(input())
m  = int(input())
a = [[randint(-100,100)for i in range(n)]for i in range(m)]
print(list([(1 if min(i)%2 else 0)if j == min(i)else j for j in i]for i in a))
