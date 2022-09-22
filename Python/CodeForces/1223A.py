m = int(input())

while m > 0:
    m -= 1
    n = int(input())
    if n == 2:
        print(2)
    elif n % 2 == 0 and n > 2:
        print(0)
    else:
        print(1)



