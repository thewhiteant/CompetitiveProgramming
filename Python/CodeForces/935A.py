n = int(input())
i = 1
t = 0
while i < n:
    if n % i == 0:
        t = t + 1
    i = i + 1

print(t)