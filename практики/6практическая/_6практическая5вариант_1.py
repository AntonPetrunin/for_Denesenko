a = []
n = 10
for i in range(n):
    a.append(int(input()))
for j in range(len(a)-1):   
    if a[j]<0 and a[j+1]<0:
        print(a[j],a[j+1])
