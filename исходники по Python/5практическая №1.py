s=input()
k=0
if s[0]=="е" or s[0]=="Е":
    k+=1
for i in range(0,len(s)):
    if s[i]==" " and s[i+1]=="е":
        k+=1
print(k)
