n = int(input())
t = 0
for i in range(n):
    s = input().split()
    d = 0
    for j in range(len(s)):
        if int(s[j]) == 1:
            d += 1
    if d >= 2:
        t += 1

print(t)