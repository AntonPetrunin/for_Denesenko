n = int(input())
def s(x):
    a = []
    b =[]
    k=0
    g = 0
    for i in range(1, n + 1):
        a.append(i)
         while i > 0:
            a.append(i%10)
            i=i//10
         for j in range(1,len(a)):
            if a[0]%a[j]==0:+