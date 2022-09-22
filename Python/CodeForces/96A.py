n = input()
one = 0
x = len(n)-1
for i in range(x):
 if one != 6:
    if n[i] == n[i + 1]:
        one += 1
    else:
        one =  one * 0
if one == 6:
 print("YES")
else:
 print("NO")