def aVeryBigSum(n,s):
    t = 0
    for i in range(n):
        t = t + s[i]
    return t


number = int(input())
sint = list(map(int,input().split()))
print(aVeryBigSum(number,sint))