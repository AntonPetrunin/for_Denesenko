a = []
b = []
n = int(input())
g = int(input())
for i in range(n):
    a.append(input())
for j in range(g):
    b.append(input())
def s(x):
    x.sort()
    print(x)
s(a)
s(b)