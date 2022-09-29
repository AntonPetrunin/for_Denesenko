s=input()
k=1
m=0
for i in range(len(s)-1):
    if s[i]=="н" and s[i+1]=="н":
        k+=1        
    else:
        if m<k:
            m=k
            k=1
s=s.replace("!",".")
print(s)
print(m)
