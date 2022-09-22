n = int(input())
s = input()
z =  0
m  = 0
for i in range(n):
     if (s[i] == "z"):
         z = z + 1
     elif(s[i] == "n"):
         m = m + 1

while m > 0 :
        print(f"{1} ")
        m = m - 1
while z > 0:
        print(f"{0} ")
        z = z - 1