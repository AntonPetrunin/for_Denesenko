n = int(input())
a = []
b = []
for i in range(n):
    a.append(int(input()))
for j in range(len(a)):
    if a.count(j)>1:
        k = j
    for g in range(len(a)):
        if a[g]==k:
            b.append(g)
            print(k)
    for l in range(len(b)):
        print(b[l],end=" ")
    b.clear()
    k = 0
