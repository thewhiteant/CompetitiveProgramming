x , y = [int(x) for x in input().split()]

z = 0
while x <= y:
    x = 3*x
    y = 2*y
    z = z + 1
print(z)
