a = []
n = int (input())
k = 0
for i in range(n):
    a.append(int(input()))
print(a)
for j in range(len(a)):
    if abs(a[j]<k):
        k = a[j]
a.reverse()
print(a,k)