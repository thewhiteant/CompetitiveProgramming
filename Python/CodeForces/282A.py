n = int(input())
p = 0
for i in range(n):
    s = input()
    if s == "X++" or s == "++X":
        p +=1
    elif s == "X--" or s == "--X":
        p -= 1
print(p)