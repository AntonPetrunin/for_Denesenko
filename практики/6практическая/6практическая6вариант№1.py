a = []
n = 10
k = 0
m = 0
for i in range(n):
    a.append(int(input()))
for g in range(len(a)):
    k = max(a[g],k)
for j in range(len(a)):
    if a[j] == k:
        m+=1
print(m,n-m)
print(k)
