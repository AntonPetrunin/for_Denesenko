s=input()
k=0
for i in range(0,len(s)):
    if s[i] == ":":
        k+=1
s=s.replace(':','%')
print(k)
print(s)
        
