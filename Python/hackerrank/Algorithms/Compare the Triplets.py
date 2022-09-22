a = list(map(int,input().split()))
b = list(map(int,input().split()))

x = 0
y = 0

for i in range(len(a)):
        if a[i] > b[i]:
            x = x + 1
        elif a[i] < b[i]:
            y = y + 1
        else:
            pass
print(x,y)
