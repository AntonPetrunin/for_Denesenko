a = []
n = int(input())
q = 0
for i in range(n):
    a.append(int(input()))
print(a)
q = a[a.index(max(a))] 
a[a.index(max(a))] = a[a.index(min(a))]
a[a.index(min(a))] = q
print(a)