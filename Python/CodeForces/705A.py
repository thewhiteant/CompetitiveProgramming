
n = int(input())
s1 = "I love"
s2 = "I hate"

for i in range(n):
    if (i % 2)== 0:
        print(s2+" " , end="")
    else:
        print(s1 + " " , end="")
    if(i != n - 1):
        print("that " , end="")
print("it " ,end="")

