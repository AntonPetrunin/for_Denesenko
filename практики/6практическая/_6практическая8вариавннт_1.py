a = []
n = int (input())
s = 0
p = 1
for i in range(n):
    a.append(int(input()))
for j in range(len(a)):
    s += a[j]
    p *= a[j]
print(s,p)