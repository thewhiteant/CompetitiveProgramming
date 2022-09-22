rang = int(input())
for i in range(rang):
    data =int(input())
    if data < 3:
        print(0)
    else:
        print(int((data-1)/2)) 