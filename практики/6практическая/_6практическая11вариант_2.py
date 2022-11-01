a = []
n = int (input())
b = []
k = 0
for i in range(n):
    a.append(int(input()))
for j in range(len(a)):
    if a[j]%2==0 and a[j]<10:
        b.append(a[j])
        k += 1
if k == 0:
    print("NO")        
print(b)