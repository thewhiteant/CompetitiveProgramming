n = int(input())
ar = list(map(int,input().split()))
i1 = 0
i2 = 0
for i in range(n):
    for j in range(n):
        if i == j:
            i1 += ar[i][j]
        if i == n - j - 1:
            i2 += ar[i][j]
print(i1,i2)