def s(n):
    g = ""
    while n != 0:
        g = str(n%8) + g
        n //= 8
    while len(g)<10:
        g = "0"+g
    return g
n = int(input())
print(s(n))