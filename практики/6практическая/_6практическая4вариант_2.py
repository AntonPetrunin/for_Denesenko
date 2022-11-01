a = []
b = []
k = 0
n=int(input())
for i in range(n):
    a.append(int(input()))
for j in range(len(a)):    
    if a[j] % 2 ==1:
        b.append(a[j])
        k+=1
if k == 0:
    print("No")
b.reverse()
print(b)