ar = list(map(int,input().split()))
l = len(ar)
p = 0
q = 0

for i in range(len(ar)):
    p = p + ar[i]
    q = q + ar[i]
p = p - ar[l-1]
q = q - ar[0]
print(p,q)