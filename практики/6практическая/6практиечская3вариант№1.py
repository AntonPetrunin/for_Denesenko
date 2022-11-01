n=int(input())
d=[]
s=0
for i in range(n):
    d.append(int(input()))
    if i%2==1:
        s+=d[i]
print(d)
print(s)