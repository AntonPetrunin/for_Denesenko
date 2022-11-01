def s(x,y):
    while x!=y :
        if x>y:
            x-=y
        else:
            y-=x
    print(x)
a = int(input())
b = int(input())
c = int(input())
d = int(input())
g = (a/b)/(c/d)
print(g)
s(a,c)
s(b,d)