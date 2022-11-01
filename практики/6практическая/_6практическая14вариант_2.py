a = []
s = 0
for i in range(10):
    a.append(int(input()))
print(a)
for j in range(len(a)):
    s += a[j]
k = s/10
for g in range(len(a)):
    if a[g]>k:
        a[g]=1
print(a)
print(k)