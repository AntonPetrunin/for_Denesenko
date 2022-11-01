from math import*
a = []
b = []
for i in range(2):
    a.append(int(input()))
for j in range(2):
    b.append(int(input()))
def s():
    if sqrt(a[0]**2+a[1]**2)>sqrt(b[0]**2+b[1]**2):
        print("a","a>b")
    else:
        print("b","b>a")
s()