a = []
n = 10
k = 0
for i in range(n):
    a.append(int(input()))
for j in range(len(a)):
    if a[j]>5:
        k += a[j]
print(a)
print(k)
