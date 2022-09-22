ssi = input()
s = 0
f = 0
for i in ssi:

    if (i == "7"):
        s+=1
    elif (i == "4"):
        f+=1
if (s+f) == 4:
    print("YES")
elif(s+f) == 7:
    print("YES")
else:
    print("NO")