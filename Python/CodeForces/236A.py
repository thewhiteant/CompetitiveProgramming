s = input()
s = sorted(s)
e = 1
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        e += 1
if e%2 == 1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")


