n = int(input())
p = 0
while n != 0:
    if n >= 100:
        q = n / 100
        q = int(q)
        n = n - (100*q)
        p = p + (1* q)
    elif n >= 20:
        n = n - 20
        p = p + 1
    elif n >= 10:
        n = n - 10
        p = p + 1
    elif n >= 5:
        n = n - 5
        p = p + 1
    elif n >= 1:
        n = n - 1
        p = p + 1

print(p)
