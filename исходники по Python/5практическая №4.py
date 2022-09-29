s=input()
k=0
for i in range(0,len(s)):
    if s[i]=="а":
        k+=1
s=s.replace("а","о")
print(len(s))
print(s)
