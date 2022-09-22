n = input().split()
n = int(n[0]) * int(n[1])

if n%2 != 0 :
    print(int((n-1)/2))
else:
    print(int(n/2))
