a = input().lower()
b = input().lower()
x = 0
y = 0

if a == b:
    print(0)
else:
    for i in range(len(a)):
        if a[i] > b[i]:
            print(1)
            break
        elif b[i] > a[i]:
            print(-1)
            break
