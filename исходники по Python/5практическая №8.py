s=input()
k=0
for i in range(0,len(s)+1):
    if s[i]==" ":
        k+=1
    if s[i]==".":
        k+=1
        break
print(k)
