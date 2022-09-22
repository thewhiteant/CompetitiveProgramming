fin = int(input())
f3 = input()
f3 = sorted(f3.lower())
count = 0
for i in range(fin-1):
    if f3[i] != f3[i+1]:
        count +=1
if count == 25:
    print("YES")
else:
    print("NO")