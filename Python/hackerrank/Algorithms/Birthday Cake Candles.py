n = int(input())
ar = list(map(int,input().split()))
m = 0
for i in range(n):
    if ar[i] <= n/2:
        m += 1
print(m)