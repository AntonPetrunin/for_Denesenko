n = int(input())
def s(x):
    k = 0
    for i in range(n,n*2+1):
        if i+2<=n*2:
            k+=1
        else:
            break
    print(k)
s(n)