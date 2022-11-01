n = int(input())
def s(x):
    k = 0
    q = x % 10
    w = (x // 10) % 10
    e = x // 100
    while x>0:
        x-=(q+w+e)
        k+=1
    print(k)
s(n)