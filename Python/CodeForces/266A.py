n = int(input())
s = input()
x = 0
for i in range(n-1):    #last er ta check kra drker nai
    if s[i] == s[i+1]:
        x += 1

print(x)