n = int(input())

x = 0
y = 0
z = 0
for i in range(n):
    nma = list(map(int,input().split()))
    x+= nma[0]
    y += nma[1]
    z +=nma[2]


if (x == 0) and (y == 0) and (z == 0):
    print("YES")
else:
     print("NO")
