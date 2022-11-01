a = []
n = int(input())
p = 1
s = 0
for i in range(n):
    a.append(int(input()))
for j in range(len(a)):
    if j%2==1:
        p*=a[j]
    else:
        s+=a[j]
print(s)
print(p)

