n = input()
def s(x):
    a = ""
    b = []
    for i in range(len(n)):
        if n[i] !=" ":
            a += str(n[i])
        if n[i]==" " or i==len(n)-1:
            b.append(a)
            a = ""
    b.reverse()
    print(" ".join(b))
s(n)
            
