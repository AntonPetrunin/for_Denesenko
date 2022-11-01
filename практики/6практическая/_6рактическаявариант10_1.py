a =[]
n = int (input())
k = 0
s = 0
for i in range(n):
    a.append(int(input()))
print(a)
for j in range(len(a)):
    if a.count(a[j])>k:
        k = a.count(a[j])
        s = a[j]
print(s)
print(k)
