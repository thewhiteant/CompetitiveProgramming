ch = input()
ct = input().split()
ct0 = ct[0]
ct1 = ct[1]
ct2 = ct[2]
ct3 = ct[3]
ct4 = ct[4]

x1 = ct0[0]
x2 = ct0[1]

y1 = ct1[0]
y2 = ct1[1]

z1 = ct2[0]
z2 = ct2[1]

u1 = ct3[0]
u2 = ct3[1]

k1 = ct4[0]
k2 = ct4[1]
if ch[0] == x1 or ch[0] == y1 or ch[0] == z1 or ch[0] == u1 or ch[0] == k1 :
    print("YES")
elif  ch[1] == x2 or ch[1] == y2 or ch[1] == z2 or ch[1] == u2 or ch[1] == k2:
    print("YES")
else:
    print("NO")