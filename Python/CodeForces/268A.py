ln = int(input())

x = []
y = []
for i in range(ln):
    lnx = list(map(int,input().split()))
    x.append(lnx[0])
    y.append(lnx[1])

count = 0

for s in x:
   for k in y:
       if k == s:
           count +=1
print(count)

