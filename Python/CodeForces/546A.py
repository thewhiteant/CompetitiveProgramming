inp = input().split()
k = int(inp[0])
n = int(inp[1])
w = int(inp[2])
mn = 0
for i in range(w+1):
    mn = mn + (i*k)
x = mn-n
if x > 0:
    print(x)
else:
    print(0)