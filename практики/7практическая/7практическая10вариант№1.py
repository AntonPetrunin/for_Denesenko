n = int(input())
a = int(input())
b = int(input())
c = int(input())
s = str(a) + str(b) + str(c)
a = [a,b,c]
def s():
    k = 0
    q = 0
    w =0
    e = 0
    for i in range(100,n+1):
        q = i%10
        w = (i//10)%10
        e = i//100
        if a.count(w)+a.count(q)+a.count(e)==3:
            k+=1
            q =0
            w = 0
            e = 0
        else:
            q = 0
            w = 0
            e = 0
    print(k)
s()