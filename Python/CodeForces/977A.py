#for exmple input:==> 52 3
# ouput :==> 5 |
# (52-1) 3 =
# => (51-1) 2 =
# =>  (50/10) 1 =
# = 5_>>
x, y = [int(x) for x in input().split()]
i = 1
while i <= y:
    y = y - 1
    if x % 10 == 0:
        x = x / 10
    else:
        x = x - 1
print(int(x))