sa = input()
word = "hello"
t = 0
p = 0
for i in sa:
    if t < 5:
        if i == word[t]:
            t+=1
            p+=1
if p == 5:
    print("YES")
else:
    print("NO")
