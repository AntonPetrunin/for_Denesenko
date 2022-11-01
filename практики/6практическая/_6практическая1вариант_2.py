a = []
n = int(input())
k = 0
s = 0
for i in range(n):
    a.append(int(input()))
print(a)
for j in range(len(a)):
    k+=a[j]
s = k/n
for g in range(len(a)):
    if a[g]==0:
        a[g]=s
print(a)
