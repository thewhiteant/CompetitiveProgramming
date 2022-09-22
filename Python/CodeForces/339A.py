s = input()
p = s.replace("+","")
one = 0
two = 0
three = 0
ans = ""
for i in range(len(s)):
    if s[i] == "1":
        one += 1
    elif s[i] == "2":
        two +=1
    elif s[i] == "3":
        three +=1
    else:
        pass

for j in range(one):
    ans = ans + "1+"
for j in range(two):
    ans = ans + "2+"
for j in range(three):
    ans = ans + "3+"

ans = ans[:-1]
print(ans)