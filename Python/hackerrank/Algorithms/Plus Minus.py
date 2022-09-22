n = int(input())
a = list(map(int,input().split()))

p = 0
N = 0
z = 0

for i in range(n):
    if a[i] < 0:
        N += 1
    elif a[i] == 0:
        z += 1
    else:
        p += 1
print(f"{p/n} \n {N/n} \n {z/n}")
